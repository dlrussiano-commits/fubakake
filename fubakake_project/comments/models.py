from django.db import models
from users.models import Perfil
from recipes.models import Receita
# Create your models here.

class Comentario(models.Model):
    conteudo = models.TextField()
    likes = models.ManyToManyField(Perfil, related_name='comentarios_curtidos')
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)