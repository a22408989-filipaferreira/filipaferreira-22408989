from django.contrib import admin
from .models import Escola
from .models import Professor
from .models import Turma
from .models import Aluno

# Register your models here.
class EscolaAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    ordering = ("nome",)
    search_fields = ("nome",)

class TurmaAdmin(admin.ModelAdmin):
    list_display = ("nome", "escola", "professor")
    ordering = ("nome",)
    search_fields = ("nome", "escola__nome", "professor__nome")
    list_filter = ("escola",)

class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "turma")
    ordering = ("nome",)
    search_fields = ("nome", "turma__nome", "turma__escola__nome")
    list_filter = ("turma",)

admin.site.register(Escola, EscolaAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Aluno, AlunoAdmin)