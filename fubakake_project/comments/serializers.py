from rest_framework import serializers
from .models import Comentario

class Comentario_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['conteudo']

