from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Perfil(AbstractUser):
    foto = models.ImageField(upload_to='fotos_perfil/', blank=True)
    bio = models.TextField(blank=True)
    receitas_salvas = models.ManyToManyField('recipes.Receita', related_name='salvos_por')