# Generated by Django 4.2.3 on 2023-09-13 23:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projeto', '0003_alter_comentario_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=models.TextField(db_column='com_comentario', max_length=6000),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='pessoa',
            field=models.ForeignKey(db_column='com_use_pessoa', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
