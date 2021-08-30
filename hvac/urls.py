from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ url(r'^$', views.index, name='index'), 
                url('hvac/', views.page_hvac, name='page_hvac'), 
                url('temp/', views.page_temp, name='page_temp'), 
                url('cool/', views.page_cool, name='page_cool'), 
                url('elec/', views.page_elec, name='page_elec'), 
                url('peak/', views.page_peak, name='page_peak'), 
                url('occpancy/', views.page_occpancy, name='page_occpancy'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
