from django.db import models

# __author:Barth
class Athlete(models.Model):

    name = models.TextField(max_length=255,
                            verbose_name='Nome do Atleta')

    athlete_code = models.IntegerField(verbose_name='Id do Atleta')

    birth_date = models.DateField(verbose_name='Nascimento')

