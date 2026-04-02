from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import Comentario_Serializer
from rest_framework.permissions import IsAuthenticated
from .models import Comentario

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def criar_comentario(request, receita_id):
    serializer = Comentario_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save(perfil=request.user, receita_id=receita_id)
        return Response({'mensagem':'Comentário criado!'}, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_comentario(request):
    comentarios = Comentario.objects.all()
    serializer = Comentario_Serializer(comentarios, many=True)
    return Response(serializer.data)