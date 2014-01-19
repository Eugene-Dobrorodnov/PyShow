from django.conf.urls import url, patterns
from users import views

urlpatterns = patterns('',
    url(r'^login$',  views.login,  name = 'login'),
    url(r'^logout$', views.logout, name = 'logout'),
    url(r'^signup$', views.signup, name = 'signup'),
)