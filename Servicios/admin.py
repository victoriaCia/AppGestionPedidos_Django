from ssl import create_default_context
from venv import create
from django.contrib import admin
from .models import Servicio

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

admin.site.register(Servicio,ServicioAdmin)





