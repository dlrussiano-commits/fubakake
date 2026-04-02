from .models import Receita
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import Receita_Serializer
from rest_framework.permissions import  IsAuthenticated

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def feed(request):
    receitas = Receita.objects.all()
    serializer = Receita_Serializer(receitas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def criar_receita(request):
    serializer = Receita_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save(perfil=request.user)
        return Response({'mensagem': 'Receita criada!'}, status=201)
    else:
        return Response(serializer.errors, status=400)