from django.contrib.auth.models import User
from django.db import models


class File(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.RESTRICT,
                             verbose_name='Usuário de Criação')
    name = models.TextField(max_length=255,
                            verbose_name='Nome do Arquivo')
    timestamp = models.DateTimeField(auto_now=True,
                                     verbose_name='Data/Hora')
    file = models.FileField(verbose_name='Arquivo')
    teste = models.TextField(max_length=255)

    class Meta:
        verbose_name = 'Arquivo de Importação'

    def __str__(self):
        return self.description


#class FileData(models.Model):
#    file = models.ForeignKey(File,
#                             on_delete=models.CASCADE,
#                             verbose_name='Arquivo')
    #athlete = models.ForeignKey(Athlete,
    #                            on_delete=models.RESTRICT,
    #                            verbose_name='Atleta')
    #competition = models.ForeignKey(Competition,
    #                                on_delete=models.RESTRICT,
    #                                verbose_name='Competição')