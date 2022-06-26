from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from Carro.carro import Carro
from Pedidos.models import LineaPedido, Pedido
from django.contrib import messages

# Create your views here.

@login_required(login_url="/autenticacion/logear")   #si no esta autenticado, redirige al login
def procesar_pedido(request):         #se llama a la funcion cuando el usuario toca el boton "hacer pedido"
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key,value in Carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
        ))

    LineaPedido.objects.bulk_create(lineas_pedido)  #muchas instrucciones insert

    enviar_mail(            #envia mail al usuario
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombre_usuario=request.username,
        email_usuario=request.usermail
    )

    messages.succes(request,"El pedido se ha creado correctamente")

    return redirect("../tienda")



