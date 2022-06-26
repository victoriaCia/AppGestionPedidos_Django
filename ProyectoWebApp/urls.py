from django.urls import path

from ProyectoWebApp.views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home, name="Home"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

