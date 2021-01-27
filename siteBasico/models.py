from django.db import models
from django.db.models.fields import CharField
from django.db.models.deletion import CASCADE

class Admin(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    senha = models.CharField(max_length=250)
    
    def __str__(self):
        return self.nome

class Galeria(models.Model):
    link_foto = models.CharField(max_length=250)

    def __str__(self):
        return self.link_foto

class Carrosel(models.Model):
    link_foto = models.CharField(max_length=250)
    quantidade = models.IntegerField()

    def __str__(self):
        return self.link_foto

class Texto(models.Model):
    texto_tela_inicial = models.TextField()

    def __str__(self):
        return self.texto_tela_inicial


class Sobre(models.Model):
    nome = models.CharField(max_length=25)
    texto = models.TextField()
    localidade = models.TextField()

    def __str__(self):
        return self.nome

class Telefone(models.Model):
    telefone = models.CharField(max_length=14)
    sobre = models.ForeignKey(Sobre,on_delete=models.CASCADE)
    
class Email(models.Model):
    email = models.EmailField(max_length=250)
    sobre = models.ForeignKey(Sobre,on_delete=models.CASCADE)

