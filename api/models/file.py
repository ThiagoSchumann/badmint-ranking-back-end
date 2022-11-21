from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import models

fs = FileSystemStorage(location='/media/sheets')

class File(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.RESTRICT,
                             verbose_name='Usuário de Criação')
    name = models.TextField(max_length=255,
                            verbose_name='Nome do Arquivo')
    timestamp = models.DateTimeField(auto_now=True,
                                     verbose_name='Data/Hora')
    file = models.FileField(storage=fs,
                            verbose_name='Arquivo')

    class Meta:
        verbose_name = 'Arquivo de Importação'

    def __str__(self):
        return self.description