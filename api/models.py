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
    codigo = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    duracao = models.IntegerField()
    status = models.IntegerField()
    autor = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)

class DiasSemana(models.Model):
    dia = models.IntegerField(unique=True)
    hora_inicio = models.TimeField(unique=True)
    hora_fim = models.TimeField(unique=True)


class UserDisciplinas(models.Model):
    disciplina = models.ForeignKey(Disciplinas, on_delete=models.DO_NOTHING)
    user = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    sala = models.CharField(max_length=20)
    dias_aula = models.ForeignKey(DiasSemana, on_delete=models.DO_NOTHING)


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


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(
        choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey(
        'auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = ('created', )

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(
            style=self.style, linenos=linenos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)
