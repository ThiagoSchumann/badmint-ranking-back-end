from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from badmint.settings import MEDIA_ROOT
from api.models import Athlete, Category, Team, Championship, RankingClassification
from django.db.models.signals import post_save
from django.dispatch import receiver
import pandas as pd


class TypeFile(models.IntegerChoices):
    ATHLETE = 1, 'Atleta'
    CHAMPIONSHIP = 2, 'Campeonato'


class File(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.RESTRICT,
                             verbose_name='Usuário de Criação',
                             null=True)
    name = models.TextField(max_length=255,
                            verbose_name='Nome do Arquivo',
                            null=True)
    timestamp = models.DateTimeField(auto_now=True,
                                     verbose_name='Data/Hora',
                                     null=True)
    file = models.FileField(
        null=True)
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
        athlete_sheet = pd.read_excel(
            MEDIA_ROOT + '/' + instance.file.name,
            skiprows=3,
            sheet_name='Players'
        )
        df = pd.DataFrame(
            athlete_sheet,
            columns=['Name', 'DOB', 'Member ID', 'Club']
        )

        for idx in df.index:
            Athlete.objects.update_or_create(
                name=pd.Series(data=df.iloc[idx].squeeze())["Name"],
                birth_date=pd.Series(data=df.iloc[idx].squeeze())["DOB"],
                athlete_code=pd.Series(data=df.iloc[idx].squeeze())["Member ID"],
                club=pd.Series(data=df.iloc[idx].squeeze())["Club"],
            )
    elif instance.type == TypeFile.CHAMPIONSHIP:
        championship_sheet = pd.read_excel(
            MEDIA_ROOT + '/' + instance.file.name,
            header=None
        )
        df_championship = pd.DataFrame(
            championship_sheet
        )
        tab = pd.ExcelFile(MEDIA_ROOT + '/' + instance.file.name).sheet_names
        print(tab[0][16:])
        championship = Championship.objects.get_or_create(
            name=tab[0][16:]
        )

        for idx in df_championship.index:
            if isinstance(df_championship.iloc[idx].squeeze()[0], str):
                try:
                    category = Category.objects.get(name=df_championship.iloc[idx].squeeze()[0][19:])
                except ObjectDoesNotExist:
                    category = Category.objects.create(name=df_championship.iloc[idx].squeeze()[0][19:])
            elif isinstance(df_championship.iloc[idx].squeeze()[0], float):
                if pd.Series(data=df_championship.iloc[idx].squeeze())[2] == 'Position':
                    pass
                else:
                    try:
                        athlete = Athlete.objects.get(
                            athlete_code=df_championship.iloc[idx].squeeze()[4]
                        )
                    except ObjectDoesNotExist:
                        try:
                            athlete = Athlete.objects.get(
                                name=df_championship.iloc[idx].squeeze()[3]
                            )
                        except ObjectDoesNotExist:
                            athlete = Athlete.objects.update_or_create(
                                athlete_code=df_championship.iloc[idx].squeeze()[4],
                                name=df_championship.iloc[idx].squeeze()[3]
                            )

                    Team.objects.get_or_create(
                        athlete_1=athlete,
                        name=athlete.name
                    )

                    ranking_classification = RankingClassification.objects.get_or_create(
                        classification=1,
                        scorePoints=123123,
                        athlete1MemberID=athlete.athlete_code,
                        athlete1Name=athlete.name,
                        athlete1Age=athlete.age(),
                        athlete1Club=athlete.club,
                        category=category.name
                    )
