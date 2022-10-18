# Generated by Django 4.1.1 on 2022-10-17 23:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255, verbose_name='Nome do Arquivo')),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='Data/Hora')),
                ('file', models.FileField(upload_to='', verbose_name='Arquivo')),
                ('teste', models.TextField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL, verbose_name='Usuário de Criação')),
            ],
            options={
                'verbose_name': 'Arquivo de Importação',
            },
        ),
    ]
