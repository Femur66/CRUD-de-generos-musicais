from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Genero(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    nome = models.CharField(max_length=100)

class Musica(models.Model):
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    artista = models.CharField(max_length=200)
    mp3 = models.FileField()
