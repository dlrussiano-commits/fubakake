from rest_framework import serializers
from .models import Receita

class Receita_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ['titulo', 'foto', 'ingredientes', 'como_fazer', 'postado_a']