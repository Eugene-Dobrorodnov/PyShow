from django import template

from showcase.models import Category, SubCategory

register = template.Library()

@register.inclusion_tag('showcase/category_list_tpl.html')
def show_cat(token):
    category = Category.objects.all()
    sub_cat  = SubCategory.objects.all()

    return {
        'category'     : category,
        'sub_category' : sub_cat,
        'request_url'  : token.split('/')
    }

