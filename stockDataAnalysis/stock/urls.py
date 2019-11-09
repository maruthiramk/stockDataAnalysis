from django.conf.urls import url


from .views import *


urlpatterns = [
    url(r'^home/$', home, name='home'),
    url(r'stock/(?P<name>\w{0,50})/$',analysis,name='stock')
]
