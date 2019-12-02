from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Cursos(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    duracao = models.IntegerField()
    status = models.IntegerField()
    autor = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)


class Disciplinas(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=100, null=True)
    carga_horaria = models.IntegerField(null=True)
    status = models.IntegerField()
    autor = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    # curso = models.ForeignKey(Cursos, on_delete=models.DO_NOTHING)

class UserDisciplinas(models.Model):
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.DO_NOTHING)
    user = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    sala = models.CharField(max_length=20, null=True)
    dia = models.IntegerField(default=0, null=True)
    hora_inicio = models.CharField(max_length=6, null=True)
    hora_fim = models.CharField(max_length=6, null=True)


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


class Chat(models.Model):
    # autor is only the admin
    channel = models.CharField(max_length=20)
    user = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    mensagem = models.CharField(max_length=255)

