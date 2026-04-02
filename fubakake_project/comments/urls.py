from django.urls import path
from .import views

urlpatterns = [

    path('create_comments/<int:receita_id>/', views.criar_comentario, name='create_comments'),
    path('comments', views.listar_comentario, name='comments')


]