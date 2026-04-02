from django.urls import path
from .import views

urlpatterns = [

    path("", views.feed, name='feed'),
    path('criar_receita', views.criar_receita, name='criar_receita')

]





