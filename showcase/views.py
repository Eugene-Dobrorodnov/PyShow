from django.shortcuts     import get_object_or_404
from django.http          import Http404, HttpResponse
from django.views.generic import ListView, DetailView
import json

from showcase.models import Item, Category, SubCategory, Comment
from showcase.forms  import CreateCommentForm

from django.views.decorators.csrf import csrf_exempt

class ItemListView(ListView):
    template_name = 'showcase/item-list.html'

    def get_queryset(self):

        if self.kwargs.get("cat"):
            cat = get_object_or_404(Category, slug = self.kwargs.get("cat"))

            if self.kwargs.get("sub_cat"):
                sub = get_object_or_404(SubCategory, slug = self.kwargs.get("sub_cat"), category_id = cat.id)
                result = sub.item_set.all()
            else:
                committee_relations = SubCategory.objects.filter(category_id = cat.id)
                result = Item.objects.filter(category = committee_relations)
        else:
            result = Item.objects.all()

        return result

class ItemDetailView(DetailView):
    model         = Item
    template_name = 'showcase/item-detail.html'

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context['sub_category']  = self.object.category
        context['category']      = self.object.category.category
        context['comments_list'] = Comment.objects.filter(item = self.object).order_by('-create_date')
        return context

@csrf_exempt
def create_comment( request):

    if request.is_ajax() and request.POST:

        get_object_or_404(Item, id = request.POST['item'])
        form = CreateCommentForm(request.POST)

        if form.is_valid():
            form.save()
            msg = json.dumps({'status':'ok'})
        else:
            msg = json.dumps({'status':'error', 'errors':form.errors})
        return HttpResponse(msg)
    else:
        raise Http404