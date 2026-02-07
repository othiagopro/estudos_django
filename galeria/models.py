from django.db import models
from datetime import datetime

class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALAXIA', 'Galáxia'),
        ('PLANETA', 'Planeta'),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False) # Nome da Fotografia, tamanho máximo 100
    legenda = models.CharField(max_length=150, null=False, blank=False) # Legenda da Fotografia, tamanho máximo 150
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='') # Categoria da Fotografia, tamanho máximo 100
    descricao = models.TextField(null=False, blank=False) # Descrição da Fotografia, campo opcional
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False) # Data e hora da Fotografia
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', blank=True) # Campo para upload da foto, as fotos serão salvas na pasta 'fotos' dentro da pasta de mídia
    publicada = models.BooleanField(default=False) # Indica se a fotografia está publicada ou não


    def __str__(self):
        return f"Fotografia: [nome={self.nome}]"
