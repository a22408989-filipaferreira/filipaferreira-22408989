from django.contrib import admin
from .models import Categoria
from .models import Produto
from .models import Cliente
from .models import Morada
from .models import Pedido
from .models import ItemPedido

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preco", "categoria")
    ordering = ("nome",)
    search_fields = ("nome", "categoria__nome")
    list_filter = ("categoria",)


class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)


class MoradaAdmin(admin.ModelAdmin):
    list_display = ("rua", "cidade", "cliente")
    ordering = ("cidade",)
    search_fields = ("rua", "cidade", "cliente__nome")


class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "data")
    ordering = ("-data",)
    search_fields = ("cliente__nome",)
    list_filter = ("data",)


class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ("pedido", "produto", "quantidade")
    search_fields = ("produto__nome", "pedido__cliente__nome")
    list_filter = ("produto",)


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Morada, MoradaAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ItemPedido, ItemPedidoAdmin)