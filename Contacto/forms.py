from django import forms

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label="Nombre", required=True)
    apellido=forms.CharField(label="Apellido",required=False)
    email=forms.EmailField(label="Email",required=True)
    contenido=forms.CharField(label="Contenido",widget=forms.Textarea,required=True)
