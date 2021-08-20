from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ url(r'^$', views.index, name='index'), 
                url(r'^$', views.page_hvac, name='page_hvac'), 
                url(r'^$', views.page_temperature, name='page_temperature'), 
                url(r'^$', views.page_cooling, name='page_cooling'), 
                url(r'^$', views.page_elec, name='page_elec'), 
                url(r'^$', views.page_peak, name='page_peak'), 
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
