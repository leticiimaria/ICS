from django.db import models
#aq vai criar e gerar o banco de dados
# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=200, db_column="usu_nome")
    email = models.EmailField(db_column="usu_email")
    senha = models.CharField(max_length=256, db_column="usu_senha")

    class Meta:
        db_table = 'tb_usuarios'
    

        