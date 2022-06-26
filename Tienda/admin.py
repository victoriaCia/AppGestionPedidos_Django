from django.contrib import admin
from .models import CategoriaProd, Producto

# Register your models here.

class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_filter=('created','updated')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('nombre','categorias','disponibilidad')
    search_fields=('nombre',)
    list_filter=('precio','categorias','disponibilidad','updated')
    date_hierarchy='updated'

admin.site.register(CategoriaProd,CategoriaProdAdmin)
admin.site.register(Producto,ProductoAdmin)




