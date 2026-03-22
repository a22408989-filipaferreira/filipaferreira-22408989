from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ingrediente(models.Model):
    # an auto-incremented id is automatically created
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Receita(models.Model):
    # an auto-incremented id is automatically created
    nome = models.CharField(max_length=100)

    ingredientes = models.ManyToManyField(
        Ingrediente,
        related_name='receitas'
    )

    favoritas = models.ManyToManyField(
        User,
        related_name='receitas_favoritas',
        blank=True
    )

    def __str__(self):
        return self.nome