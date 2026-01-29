from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    
    dados = {
        1: {'nome': "Nebulosa de Carina", 
            'legenda': "webbtelecope.org / NASA / James Webb"},
        2: {'nome': "Nebulosa de Orion", 
            'legenda': "webbtelecope.org / NASA / James Webb"},
    }

    return render(request, 'galeria/index.html', {'cards': dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')
