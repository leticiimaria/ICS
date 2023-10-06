from django import forms 
from django.forms import fields, models, ModelForm 
from .models import Pessoa,Comentario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
   nome = forms.CharField(max_length=200, required=True)
   email = forms.EmailField(required=True)
   senha = forms.PasswordInput()
    #perfil = forms.ChoiceField(choices=((0,"Professor"),(1,'Aluno')))
    #email = forms.EmailField(required=True, attrs={'class':'form-control'})
    
