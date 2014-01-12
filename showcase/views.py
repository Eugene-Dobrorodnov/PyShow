from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from showcase.models import Item, Category, SubCategory

class ItemListView(ListView):
    template_name = 'showcase/item-list.html'

    def get_queryset(self):
        if self.kwargs.get("cat"):
            cat = get_object_or_404(Category, alias=self.kwargs.get("cat"))

            if self.kwargs.get("sub_cat"):
                sub = get_object_or_404(SubCategory, alias=self.kwargs.get("sub_cat"), category_id=cat.id)
                result = sub.item_set.all()
            else:
                committee_relations = SubCategory.objects.filter(category_id=cat.id)
                result = Item.objects.filter(category=committee_relations)
        else:
            result = Item.objects.all()

        return result

class ItemDetailView(DetailView):
    model         = Item
    template_name = 'showcase/item-detail.html'