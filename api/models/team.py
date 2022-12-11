from django.db import models
from api.models import Athlete, Category


class Team(models.Model):
    athlete_1 = models.ForeignKey(Athlete,
                                  on_delete=models.CASCADE,
                                  verbose_name='Atleta 1',
                                  related_name='athlete_1',
                                  null=True)
    athlete_2 = models.ForeignKey(Athlete,
                                  on_delete=models.CASCADE,
                                  verbose_name='Atleta 2',
                                  null=True,
                                  related_name='athlete_2')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name='Categoria',
                                 null=True,
                                 related_name='category')
    name = models.TextField(max_length=255,
                            verbose_name='Nome',
                            null=True)

    class Meta:
        verbose_name = 'Time'

    def __str__(self):
        return self.name
