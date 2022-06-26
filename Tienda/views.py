from django.shortcuts import render, HttpResponse
from .models import Producto

# Create your views here.

def tienda(request):
    productos=Producto.objects.all()

    return render(request, "tienda/tienda.html",{'productos':productos})


def buscar(request):
    if request.GET["prod"]:
        producto=request.GET["prod"]
        if len(producto)>20:
            mensaje="Texto de busqueda demasiado largo"
        else:
            productos=Producto.objects.filter(nombre__icontains=producto) #__icontains es como si fuera un like en SQL
            return render(request, "tienda/resultados_busq_prod.html", {"articulos":productos, "query":producto})
    else:
        mensaje="No has introducido nada"
    return HttpResponse(mensaje)

