from django.conf.urls import patterns, url

from cart.views import Cart, check_orders, show_orders

urlpatterns = patterns('',
    url(r'^$',                     Cart.as_view(), name = 'index'),
    url(r'^/item/(?P<id>[0-9]+)$', Cart.as_view(), ),
    url(r'^/my-orders$',           show_orders,    name = 'show'),
    url(r'^/check-orders$',        check_orders,   name = 'check'),
)