from django.shortcuts import render, redirect
from .carro import Carro
from Tienda.models import Producto

# Create your views here.

def agregrar_producto(request,producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar_producto(producto=producto)
    return redirect("Tienda")

def eliminar_producto(request,producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar_producto(producto=producto)
    return redirect("Tienda")

def restar_producto(request,producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("Tienda")

def limpiar_carro(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("Tienda")


