from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),    
    url(r'^contact/$', views.contact, name = 'contact'),    
    url(r'^friends/$', views.friends, name = 'friends'),
    url(r'^messages/$', views.messages, name = 'messages'),
    url(r'^images/$', views.images, name = 'images'), 
    url(r'^images/add/$', views.add_image)                
]
