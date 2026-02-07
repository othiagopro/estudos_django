from django.db import models

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
    foto = models.CharField(max_length=100, null=False, blank=False)    # Nome da foto

    def __str__(self):
        return f"Fotografia: [nome={self.nome}]"
        