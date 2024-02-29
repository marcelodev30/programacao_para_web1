from django.db import models
from django.utils import timezone

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nome

class Endereco(models.Model):
    numero = models.IntegerField()
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    
    def __str__(self):
        return self.rua 