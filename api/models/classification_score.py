from django.db import models

from api.models import Team, Championship, Category


class ClassificationScore(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE,
                            null=True)
    championship = models.ForeignKey(Championship, on_delete=models.CASCADE,
                            null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                            null=True)
    classification = models.IntegerField(verbose_name='Posição da classificação',
                            null=True)
    score = models.FloatField(verbose_name='Pontuação da Posição',
                            null=True)
    expiration_date = models.DateField(null=True)

    class Meta:
        verbose_name = 'Pontuação de Classificação'

    def __str__(self):
        return self.championship.name + ' -> ' + self.team.name
