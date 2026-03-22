from django.contrib import admin
from .models import Festival
from .models import Banda
from .models import Genero

# Register your models here.
class GeneroAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)


class BandaAdmin(admin.ModelAdmin):
    list_display = ("nome", "genero")
    ordering = ("nome",)
    search_fields = ("nome", "genero__nome")
    list_filter = ("genero",)


class FestivalAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome", "bandas__nome")
    filter_horizontal = ("bandas",)


admin.site.register(Genero, GeneroAdmin)
admin.site.register(Banda, BandaAdmin)
admin.site.register(Festival, FestivalAdmin)