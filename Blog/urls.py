from django.urls import path
from .views import blog, categoria

urlpatterns = [
    path('',blog, name="Blog"),
    path('categoria/<int:categoria_id>/', categoria, name="categoria")
]
