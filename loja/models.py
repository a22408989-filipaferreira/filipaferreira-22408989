from django.db import models

# Create your models here.
class Categoria(models.Model):
    # an auto-incremented id is automatically created
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    # an auto-incremented id is automatically created
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='produtos'
    )

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    # an auto-incremented id is automatically created
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Morada(models.Model):
    # an auto-incremented id is automatically created
    rua = models.CharField(max_length=150)
    cidade = models.CharField(max_length=100)

    cliente = models.OneToOneField(
        Cliente,
        on_delete=models.CASCADE,
        related_name='morada'
    )

    def __str__(self):
        return f"{self.rua}, {self.cidade}"


class Pedido(models.Model):
    # an auto-incremented id is automatically created
    data = models.DateField()

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='pedidos'
    )

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nome}"


class ItemPedido(models.Model):
    # an auto-incremented id is automatically created
    quantidade = models.PositiveIntegerField()

    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name='itens'
    )

    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE,
        related_name='itens_pedido'
    )

    def __str__(self):
        return f"{self.produto.nome} x{self.quantidade}"