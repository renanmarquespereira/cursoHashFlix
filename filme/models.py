# TABELAS DO BANCO DE DADOS
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
LISTA_CATEGORIAS = (
    # 'COMOARMAZENARA NO BD', 'COMO O USUARIO VERÀ'
    ("ANALISES", "Análises"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),
)

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    # pra imagem tem que passar o local onde sera armazenado as imagem no prohgrama
    thumbnail = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=20, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    # Função que denomina o que eu quero que mostre quando printar uma estancia desse objeto
    def __str__(self):
        return self.titulo

class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()

    def __str__(self):
        return self.filme.titulo + " - " + self.titulo


class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme")

