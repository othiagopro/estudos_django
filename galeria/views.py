from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True) # Filtra apenas as fotografias que estão publicadas
    return render(request, 'galeria/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id) # Primeiro buscamos a fotografia pelo ID
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

