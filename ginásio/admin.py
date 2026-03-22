from django.contrib import admin
from .models import Ginasio
from .models import PT
from .models import Cliente
from .models import Sessao

# Register your models here.
class GinasioAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)


class PTAdmin(admin.ModelAdmin):
    list_display = ("nome", "ginasio")
    ordering = ("nome",)
    search_fields = ("nome", "ginasio__nome")
    list_filter = ("ginasio",)


class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "ginasio")
    ordering = ("nome",)
    search_fields = ("nome", "ginasio__nome")
    list_filter = ("ginasio",)


class SessaoAdmin(admin.ModelAdmin):
    list_display = ("data", "hora", "pt", "cliente")
    ordering = ("data", "hora")
    search_fields = ("pt__nome", "cliente__nome", "pt__ginasio__nome", "cliente__ginasio__nome")
    list_filter = ("data", "pt", "cliente")


admin.site.register(Ginasio, GinasioAdmin)
admin.site.register(PT, PTAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Sessao, SessaoAdmin)