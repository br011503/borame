from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [    
#     path('', views.hello, name='hello'),
    url(r'^$', views.index, name='index'),
]
