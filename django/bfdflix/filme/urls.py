# filme/urls.py

from django.urls import path
from . import views # Importa as views do seu app

app_name = 'filme' # Boa prática para namespacing de URLs

urlpatterns = [
    # Esta linha associa o caminho vazio ('') à função views.homepage
    path('', views.homepage, name='homepage'), 
    # Adicione outras URLs do app aqui
]