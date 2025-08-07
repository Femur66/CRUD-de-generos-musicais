"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import index, inserir_genero, editar_genero, deletar_genero, entrar, sair, musicas, inserir_musica, editar_musica, deletar_musica

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('inserir/', inserir_genero, name='inserir'),
    path('editar/<id>', editar_genero, name='editar'),
    path('deletar/<id>', deletar_genero, name='deletar'),
    path('entrar/', entrar, name='entrar'),
    path('sair/', sair, name='sair'),
    path('musicas/<id>', musicas, name='musicas'),
    path('inserir_musica/<id>', inserir_musica, name='inserir_musica'),
    path('editar_musica/<id>', editar_musica, name='editar_musica'),
    path('deletar_musica/<id>', deletar_musica, name='deletar_musica')
]
