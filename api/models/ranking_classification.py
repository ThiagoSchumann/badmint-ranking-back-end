from django.db import models


class RankingClassification(models.Model):
    classification = models.IntegerField(null=True,
                                         blank=True)
    scorePoints = models.IntegerField(null=True,
                                      blank=True)
    athlete1MemberID = models.TextField(null=True,
                                        max_length=50,
                                        blank=True)
    athlete1Name = models.TextField(null=True,
                                    max_length=255,
                                    blank=True)
    athlete1Age = models.IntegerField(null=True)
    athlete1Club = models.TextField(null=True,
                                    max_length=255,
                                    blank=True)
    athlete2MemberID = models.TextField(null=True,
                                        max_length=50,
                                        blank=True)
    athlete2Name = models.TextField(null=True,
                                    max_length=255,
                                    blank=True)
    athlete2Age = models.IntegerField(null=True)
    athlete2Club = models.TextField(null=True,
                                    max_length=255,
                                    blank=True)
    category = models.TextField(null=True,
                                max_length=255,
                                blank=True)
