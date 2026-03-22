from django.db import models

# Create your models here.
class Escola(models.Model):
    # an auto-incremented id is automatically created
    nome = models.CharField(max_length=100)

class Professor(models.Model):
    # an auto-incremented id is automatically created
    nome = models.CharField(max_length=100)

class Turma(models.Model):
    # an auto-incremented id is automatically created
    nome = models.CharField(max_length=50)

    escola = models.ForeignKey(
        Escola,
        on_delete=models.CASCADE,
        related_name='turmas'
    )

    professor = models.OneToOneField(
        Professor,
        on_delete=models.CASCADE,
        related_name='turma'
    )

class Aluno(models.Model):
    # an auto-incremented id is automatically created
    nome = models.CharField(max_length=100)

    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        related_name='alunos'
    )