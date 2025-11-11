# filme/views.py

from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    # Por enquanto, vamos retornar uma resposta simples
    # No futuro, esta função renderizaria um template HTML
    return HttpResponse("<h1>Filme!</h1>")