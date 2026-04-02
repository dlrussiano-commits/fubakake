from django.db import models

# Create your models here.

class Receita(models.Model):
    titulo = models.CharField(max_length=40)
    foto = models.ImageField(upload_to='fotos_receita/', blank=True)
    ingredientes = models.TextField()
    # Passo a passo de como fazer a receita
    como_fazer = models.TextField()
    perfil = models.ForeignKey('users.Perfil', on_delete=models.CASCADE)
    postado_a = models.DateTimeField(auto_now_add=True)