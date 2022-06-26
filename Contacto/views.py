from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage
# Create your views here.

def contacto(request):
    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            apellido=request.POST.get("apellido")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email_auto=EmailMessage("Mensaje desde App Django",
            "El usuario con nombre {} {} con la direccion {}, te escribe lo siguiente:\n\n {}".format(nombre,apellido,email,contenido),
            "",["victoriacia98@gmail.com"],reply_to=[email]) 

            try:
                email_auto.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?invalido")

    return render(request, "contacto/contacto.html",{'miformulario':formulario_contacto})




