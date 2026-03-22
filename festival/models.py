from django.db import models

# Create your models here.
class Genero(models.Model):
    # an auto-incremented id is automatically created
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Banda(models.Model):
    # an auto-incremented id is automatically created
    nome = models.CharField(max_length=100)

    genero = models.ForeignKey(
        Genero,
        on_delete=models.CASCADE,
        related_name='bandas'
    )

    def __str__(self):
        return self.nome


class Festival(models.Model):
    # an auto-incremented id is automatically created
    nome = models.CharField(max_length=100)

    bandas = models.ManyToManyField(
        Banda,
        related_name='festivais'
    )

    def __str__(self):
        return self.nome