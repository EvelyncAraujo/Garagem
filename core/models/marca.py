from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
    class Nacionalidade(models.Model):
      nacionalidade = models.CharField(max_length=50) 
  

    def __str__(self):
        return self.nacionalidade.upper()