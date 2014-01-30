from django.conf.urls import patterns, url

from cart.views import Cart

urlpatterns = patterns('',
    url(r'^$', Cart.as_view(), name = 'index'),
    url(r'^/item/(?P<id>[0-9]+)$', Cart.as_view(), name = 'index'),
)