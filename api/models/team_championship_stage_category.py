from django.db import models

from api.models import Category, Team, ChampionshipSheetImportation


class TeamChampionshipStageCategory(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name='Categoria',
                                 null=True)
    team = models.ForeignKey(Team,
                             on_delete=models.CASCADE,
                             verbose_name='Time',
                             null=True)
    championship_sheet_importation = models.ForeignKey(ChampionshipSheetImportation,
                                                       on_delete=models.CASCADE,
                                                       verbose_name='Planilha',
                                                       null=True)
    team_position_stage_category = models.IntegerField(
        null=True)
    team_position_category_stage = models.IntegerField(null=True)
    expiration_date = models.DateField(verbose_name='Data de Fim do Campeonato',
                                       null=True)
    json_data = models.TextField(max_length=50000,
                                 verbose_name='Nome',
                                 null=True)

    class Meta:
        verbose_name = 'Categorias de fase do campeonado por equipes'

    def __str__(self):
        return self.category, self.team, self.championship_sheet_importation
