from django.db import models


class ClassificationScore(models.Model):
    classification = models.IntegerField(verbose_name='Posição da classificação',
                            null=True)
    score = models.FloatField(verbose_name='Pontuação da Posição',
                            null=True)

    class Meta:
        verbose_name = 'Pontuação de Classificação'

    def __str__(self):
        return self.classification
