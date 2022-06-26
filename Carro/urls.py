from django.urls import path
from .views import agregrar_producto,eliminar_producto,restar_producto,limpiar_carro

app_name="carro"

urlpatterns=[
    path("agregar/<int:producto_id>/",agregrar_producto,name="agregar"),
    path("eliminar/<int:producto_id>/",eliminar_producto,name="eliminar"),
    path("restar/<int:producto_id>/",restar_producto,name="restar"),
    path("limpiar/",limpiar_carro,name="limpiar"),
]