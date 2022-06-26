from django.contrib import admin
from .models import Pedido,LineaPedido

# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    readonly_fields=('created_at',)
    list_display=('id','user','created_at')

class LineaPedidoAdmin(admin.ModelAdmin):
    readonly_fields=('created_at',)
    list_display=('pedido_id','user')
    search_fields=('user',)
    list_filter=('created_at',)

admin.site.register(Pedido,PedidoAdmin)
admin.site.register(LineaPedido,LineaPedidoAdmin)
