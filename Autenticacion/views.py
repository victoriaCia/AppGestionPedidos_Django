from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

class VRegistro(View):
    
    def get(self,request):   #encargada de crear y mostrar el formulario 
        form=UserCreationForm()
        return render(request,"registro/registro.html",{"form":form})

    def post(self,request):
        form=UserCreationForm(request.POST)    #se almacena el usuario y la contraseña
        
        if form.is_valid():
            usuario=form.save()   #se almacena la info del usuario en una variable y en la BBDD
            login(request,usuario)      
            return redirect('Home')
        else:
            for msg in form.error_messages:   #por cada mensaje de error q haya en el formulario, mostrar un mensaje
                messages.error(request,form.error_messages[msg])
            return render(request,"registro/registro.html",{"form":form})     #q muestre el formulario pero con los errores

def cerrar_sesion(request):
    logout(request)
    return redirect('Home')

def logear(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario,password=contra)
            if usuario is not None:
                login(request,usuario)
                return redirect('Home')
            else: 
                messages.error(request,"Usuario no válido")
        else:
            messages.error(request,"Información incorrecta")
    form=AuthenticationForm()
    return render(request,"login/login.html",{"form":form})
