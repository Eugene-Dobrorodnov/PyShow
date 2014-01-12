from django.conf.urls import patterns, url

from showcase import views

urlpatterns = patterns('',

    url(r'^$', views.ItemListView.as_view(), name = 'index'),
    url(r'^item/(?P<pk>\d+)$', views.ItemDetailView.as_view(), name = 'detail'),
    url(r'^(?P<cat>[\w-]+)$', views.ItemListView.as_view(),   name = 'index_cat'),
    url(r'^(?P<cat>[\w-]+)/(?P<sub_cat>[\w-]+)$', views.ItemListView.as_view(), name = 'index_cat_sub'),
)