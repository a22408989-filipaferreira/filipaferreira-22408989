from django.db import models

# Create your models here.
class Ginasio(models.Model):
    # an auto-incremented id is automatically created
    nome = models.CharField(max_length=100)


class PT(models.Model):
    # an auto-incremented id is automatically created
    nome = models.CharField(max_length=100)

    ginasio = models.ForeignKey(
        Ginasio,
        on_delete=models.CASCADE,
        related_name='pts'
    )


class Cliente(models.Model):
    # an auto-incremented id is automatically created
    nome = models.CharField(max_length=100)

    ginasio = models.ForeignKey(
        Ginasio,
        on_delete=models.CASCADE,
        related_name='clientes'
    )


class Sessao(models.Model):
    # an auto-incremented id is automatically created
    data = models.DateField()
    hora = models.TimeField()

    pt = models.ForeignKey(
        PT,
        on_delete=models.CASCADE,
        related_name='sessoes'
    )

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='sessoes'
    )