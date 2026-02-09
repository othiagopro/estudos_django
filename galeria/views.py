from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True) # Filtra apenas as fotografias que estão publicadas
    return render(request, 'galeria/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id) # Primeiro buscamos a fotografia pelo ID
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)

    if 'buscar' in request.GET:  # Verificamos se o campo de busca foi preenchido
        nome_a_buscar = request.GET['buscar'] # Pegamos o valor do campo de busca
        if nome_a_buscar: # Verificamos se o valor do campo de busca não está vazio
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar) # Filtramos as fotografias pelo nome, usando o operador icontains para fazer uma busca case-insensitive 

    return render(request, 'galeria/buscar.html', {'cards': fotografias})
