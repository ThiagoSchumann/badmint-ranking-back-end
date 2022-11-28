from django.contrib.auth.models import User
from django.db import models
from badmint.settings import MEDIA_ROOT
from api.models import Athlete
import pandas as pd
from django.db.models.signals import post_save
from django.dispatch import receiver


class TypeFile(models.IntegerChoices):
    ATHLETE = 1, 'Atleta'
    CHAMPIONSHIP = 2, 'Campeonato'


class File(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.RESTRICT,
                             verbose_name='Usuário de Criação')
    name = models.TextField(max_length=255,
                            verbose_name='Nome do Arquivo')
    timestamp = models.DateTimeField(auto_now=True,
                                     verbose_name='Data/Hora')
    file = models.FileField()
    type = models.IntegerField(null=False,
                               blank=False,
                               default=TypeFile.ATHLETE,
                               choices=TypeFile.choices,
                               verbose_name='Tipo de Usuário')

    class Meta:
        verbose_name = 'Arquivo de Importação'

    def __str__(self):
        return self.name


@receiver(post_save, sender=File)
def file_post_save(sender, instance, **kwargs):

    if instance.type == TypeFile.ATHLETE:

        read_file = pd.read_excel(
                                  MEDIA_ROOT + '/' + instance.file.name,
                                  skiprows=3,
                                  sheet_name='Players'
                                 )
        df = pd.DataFrame(read_file, columns=['Name', 'DOB', 'Member ID', 'Club'])

        for idx in df.index:
            athlete = Athlete.objects.create(
                                              name=pd.Series(data=df.iloc[idx].squeeze())["Name"],
                                              birth_date=pd.Series(data=df.iloc[idx].squeeze())["DOB"],
                                              athlete_code=pd.Series(data=df.iloc[idx].squeeze())["Member ID"],
                                              club=pd.Series(data=df.iloc[idx].squeeze())["Club"],
                                            )
