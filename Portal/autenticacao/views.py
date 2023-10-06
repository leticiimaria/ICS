from django.shortcuts import render, HttpResponseRedirect
from .models import Usuario
from .forms import UsuarioForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login
# Create your views here.

def index(request):    
    return render(request,"index.html")

def contatos(request):    
    return render(request,"contatos.html")

def editais(request):    
    return render(request,"editais.html")

def editaisAno(request):    
    return render(request,"editaisAno.html")

def noticias(request):    
    return render(request,"noticias.html")

@login_required(login_url = "login")
def index_2 (request):    
    usuarios = Usuario.objects.all()
    return render(request,"index.html",{"listaUsuario":usuarios})

def cadastro(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect("/")
    form = UsuarioForm()
    return render(request,"cadastro.html", {"form":form})

def excluir(request, id):
    usuario = Usuario.objects.get(pk=id)
    usuario.delete()
    return HttpResponseRedirect("/")
def editar(request,id):
    usuario = Usuario.objects.get(pk=id)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    form = UsuarioForm(instance=usuario)
    return render(request,"cadastro.html", {"form":form})




