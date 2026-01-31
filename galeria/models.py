from django.db import models

class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False) # Nome da Fotografia, tamanho máximo 100
    legenda = models.CharField(max_length=150, null=False, blank=False) # Legenda da Fotografia, tamanho máximo 150
    descricao = models.TextField(null=False, blank=False) # Descrição da Fotografia, campo opcional
    foto = models.CharField(max_length=100, null=False, blank=False)    # Nome da foto

    def __str__(self):
        return f"Fotografia: [nome={self.nome}]"