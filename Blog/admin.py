from django.contrib import admin
from .models import Categoria,Post

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    #search_fields=('nombre',)

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('titulo','autor','created')
    #search_fields=('titulo','autor','categorias')
    list_filter=('categorias','updated','created')

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Post,PostAdmin)


