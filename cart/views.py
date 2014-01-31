# -*- coding: utf-8 -*-
from django.shortcuts     import render, get_object_or_404
from django.http          import HttpResponse, HttpRequest, Http404
from django.views.generic import View
from django.utils         import timezone
from django.views.decorators.csrf import csrf_exempt
from cart.models          import Oreders
from decimal import Decimal
import json

from showcase.models import Item

class Cart(View):

    cart_list = {}

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_authenticated():
            return HttpResponse('Need User!')

        if request.session.get('user_cart'):
            self.cart_list = request.session['user_cart']
        else:
            self.cart_list = {
                'total_count' : 0,   # Общее колво товаров в корзине
                'total_price' : 0, # Сумма всех товаров
                'item_list'   : {}   # Словарь для хранения товаров
            }

        return super(Cart, self).dispatch(request, *args, **kwargs)

    def get(self, request, **kwargs):
        return render(request, 'cart/cart-list.html', {'list':self.cart_list})

    def post(self, request, **kwargs):

        if not request.is_ajax():
            raise Http404

        item_id = kwargs.get('id')
        item    = get_object_or_404(Item, id = item_id)

        #Делаем вставку товара в сеесию
        if item_id not in self.cart_list['item_list']:

            total_count = int(self.cart_list['total_count'])
            total_price = float(self.cart_list['total_price'])
            self.cart_list['item_list'].update({
                item_id : {
                    'current_count' : 1,
                    'slug'          : item.slug,
                    'max_count'     : int(item.count),
                    'name'          : item.title,
                    'price'         : float(item.price),
                    'sum'           : float(item.price),
                }
            })

            #меняем общее кол-во товаров
            self.cart_list.update({
                'total_count' : total_count + 1
            })

            #меняем общую цену товаров (какого черта не засовывается Decimal() в словарь???)
            self.cart_list.update({
                'total_price' : float(item.price) + total_price #Decimal(item.price).__unicode__()
            })

            msg = json.dumps({'status': 'ok', 'total_count' : int(self.cart_list['total_count'])})
        else:
            msg = json.dumps({'status': 'item in cart!'})

        request.session['user_cart'] = self.cart_list
        return HttpResponse(msg)

    def delete(self, request, **kwargs):

        if not request.is_ajax():
            raise Http404

        item_id = kwargs.get('id')
        item    = get_object_or_404(Item, id = item_id)

        if item_id in self.cart_list['item_list']:

            total_count = int(self.cart_list['total_count'])
            total_price = float(self.cart_list['total_price'])

            self.cart_list.update({
                'total_count' : total_count - int(self.cart_list['item_list'][item_id]['current_count'])
            })

            self.cart_list.update({
                'total_price' : total_price - float(item.price)
            })

            msg = json.dumps({
                'status'      : 'ok',
                'total_price' : float(self.cart_list['total_price']),
                'total_count' : int(self.cart_list['total_count'])
            })
            del self.cart_list['item_list'][item_id]


        request.session['user_cart'] = self.cart_list

        return HttpResponse(msg)

def check_orders(request):

    if not request.user.is_authenticated():
        return HttpResponse('Need User!')

    if not request.session.get('user_cart'):
        raise Http404

    obj_list  = []
    item_list = request.session['user_cart']['item_list']

    if not item_list:
        return HttpResponse('none')

    for key in item_list:
        item = Oreders(
            item_id     = Item.objects.get(id = key), #А вот это очень плохой тон...
            user_id     = request.user,
            create_date = timezone.now(),
        )
        obj_list.append(item)

    Oreders.objects.bulk_create(obj_list)
    del request.session['user_cart']
    return HttpResponse('Заказ оформлен!')


def show_orders(request):

    if not request.user.is_authenticated():
        return HttpResponse('Need User!')

    order_list = Oreders.objects.filter(user_id = request.user)
    return render(request, 'cart/order-list.html', {'order_list':order_list})