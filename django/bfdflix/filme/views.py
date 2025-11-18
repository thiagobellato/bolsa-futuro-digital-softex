# filme/views.py

from django.shortcuts import render
from django.db.models import F # Opcional: para consultas mais avançadas
from .models import Filme      # Importa o modelo que você criou

def homepage(request):
    # CORREÇÃO: Usar .all() para buscar os objetos e criar um QuerySet iterável.
    
    # Busca os 8 filmes mais recentes, ordenando pelo campo 'data_criacao'
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[:8] 
    
    contexto = {
        'lista_filmes': lista_filmes 
    }

    # Renderiza o template, passando a lista de filmes
    return render(request, 'homepage.html', contexto)