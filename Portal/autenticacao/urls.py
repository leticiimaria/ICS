from django.urls import path 
from . import views 
from django.conf.urls import include 
app_name = "projeto"
urlpatterns = [
    path("", views.index, name="index"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("excluir/<int:id>", views.excluir, name="excluir"),
    path("editar/<int:id>", views.editar, name="editar"),
    path("contatos", views.contatos, name="contatos"),
    path("editais", views.editais, name="editais"),
    path("editaisAno", views.editaisAno, name="editaisAno"),
    path("noticias", views.noticias, name="noticias"),
]