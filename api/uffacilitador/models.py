from django.db import models
from django.contrib.auth.models import AbstractUser

class Cursos(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    duracao = models.IntegerField()
    status = models.IntegerField()
    autor = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)


class Disciplinas(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    duracao = models.IntegerField()
    status = models.IntegerField()
    autor = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)


class GradeCurricular(models.Model):
    carga_horaria = models.IntegerField()
    data_criacao = models.IntegerField()
    status = models.IntegerField()
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    disciplinas = models.ManyToManyField(Disciplinas)


class Repositorios(models.Model):
    url = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    status = models.IntegerField()
    autor = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.DO_NOTHING)


class Sistemas(models.Model):
    # autor is only the admin
    url = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    status = models.IntegerField()


class Usuarios(AbstractUser):
    curso=models.ForeignKey(Cursos, on_delete=models.DO_NOTHING)
    disciplinas = models.ManyToManyField(Disciplinas)
    repositorios = models.ManyToManyField(Repositorios)
    sistemas = models.ManyToManyField(Sistemas)