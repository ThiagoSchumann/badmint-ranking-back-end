from django.db import models


class RankingClassification(models.Model):
    classification = models.IntegerField()
    scorePoints = models.IntegerField()
    athlete1MemberID = models.TextField(max_length=50)
    athlete1Name = models.TextField(max_length=255)
    athlete1Age = models.IntegerField()
    athlete1Club = models.TextField(max_length=255)
    athlete2MemberID = models.TextField(max_length=50)
    athlete2Name = models.TextField(max_length=255)
    athlete2Age = models.IntegerField()
    athlete2Club = models.TextField(max_length=255)
    category = models.TextField(max_length=255)