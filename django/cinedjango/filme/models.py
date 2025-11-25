from django.utils import timezone
from django.db import models

# Create your models here.

#Criar o filme

LISTA_CATEGORIAS = [
    ('AULAS', 'Aulas'),
    ('ANIMACAO', 'Animação'),
    ('AVENTURA', 'Aventura'),
    ('COMEDIA', 'Comédia'),
    ('DOCUMENTARIO', 'Documentário'),
    ('DRAMA', 'Drama'),
    ('FICCAO', 'Ficção'),
    ('GUERRA', 'Guerra'),
    ('ROMANCE', 'Romance'),
    ('TERROR', 'Terror'),
]
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes/')
    descricao = models.CharField(max_length=1000)
    categoria = models.CharField(max_length=20,choices=LISTA_CATEGORIAS)
    vizualizaoes = models.IntegerField(default=0)
    data_cadastro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo