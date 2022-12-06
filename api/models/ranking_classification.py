from django.db import models


class RankingClassification(models.Model):
    classification = models.IntegerField(null=True, blank=True)
    scorePoints = models.IntegerField(null=True, blank=True)
    championship = models.TextField(null=True, max_length=255, blank=True)
    period_date = models.DateField(null=True, blank=True)
    category = models.IntegerField(null=True, blank=True)
    category_description = models.TextField(null=True, max_length=255, blank=True)
    ranking = models.IntegerField(null=True, blank=True)
    ranking_description = models.TextField(null=True, max_length=255, blank=True)
    athlete1MemberID = models.TextField(null=True, max_length=50, blank=True)
    athlete1Name = models.TextField(null=True, max_length=255, blank=True)
    athlete1Age = models.IntegerField(null=True, blank=True)
    athlete1Club = models.TextField(null=True, max_length=255, blank=True)
    athlete2MemberID = models.TextField(null=True, max_length=50, blank=True)
    athlete2Name = models.TextField(null=True, max_length=255, blank=True)
    athlete2Age = models.IntegerField(null=True, blank=True)
    athlete2Club = models.TextField(null=True, max_length=255, blank=True)

    class Meta:
        verbose_name = 'Classificação Ranking'
