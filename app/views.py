from django.shortcuts import render, redirect
from app.models import Genero, Musica
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='entrar')
def index(request):
    dado = Genero.objects.filter(usuario=request.user)
    return render(request, 'index.html', {'dado': dado})

@login_required(login_url='entrar')
def inserir_genero(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        usuario = request.user
        dado = Genero(nome=nome, usuario=usuario)
        dado.save()
        return redirect('index')
    else:
        return render(request, 'inserir_genero.html')

@login_required(login_url='entrar')
def editar_genero(request, id):
    dado = Genero.objects.get(id=id, usuario=request.user)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        dado.nome = nome
        dado.save()
        return redirect('index')
    else:
        return render(request, 'editar_genero.html', {'dado':dado})

@login_required(login_url='entrar')
def deletar_genero(request, id):
    obj = Genero.objects.get(id=id, usuario=request.user)
    obj.delete()
    return redirect('index')

def entrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = authenticate(username=nome, password=senha)
        if user is not None:
            login(request, user)
            return redirect('index')
    else:
        return render(request, 'entrar.html')

@login_required(login_url='entrar')
def sair(request):
    logout(request)
    return redirect('entrar')

@login_required(login_url='entrar')
def musicas(request, id):
    genero = Genero.objects.get(id=id)
    dado = Musica.objects.filter(genero=genero)
    return render(request, 'musicas.html', {'dado': dado, 'genero': genero})

@login_required(login_url='entrar')
def inserir_musica(request, id):
    dado = Genero.objects.get(id=id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        artista = request.POST.get('artista')
        mp3 = request.POST.get('mp3')
        genero = Genero.objects.get(id=id)
        dado = Musica(nome=nome, artista=artista, mp3=mp3, genero=genero)
        dado.save()
        return redirect(f'/musicas/{id}')
    else:
        return render(request, 'inserir_musica.html', {'dado': dado})

@login_required(login_url='entrar')
def editar_musica(request, id):
    dado = Musica.objects.get(id=id, genero__usuario=request.user)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        artista = request.POST.get('artista')
        mp3 = request.POST.get('mp3')
        dado.nome = nome
        dado.artista = artista
        dado.mp3 = mp3
        dado.save()
        return redirect('index')
    else:
        return render(request, 'editar_musica.html', {'dado':dado})

@login_required(login_url='entrar')
def deletar_musica(request, id):
    obj = Musica.objects.get(id=id, genero__usuario=request.user)
    obj.delete()
    return redirect('index')
