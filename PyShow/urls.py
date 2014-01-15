import django
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/',    include(admin.site.urls)),
    url(r'^showcase/', include('showcase.urls', namespace = 'showcase')),
    url(r'^auth/',     include('users.urls',    namespace = 'user')),
)
