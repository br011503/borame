from django.urls import path, include
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ url(r'^$', views.index, name='index'), ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
