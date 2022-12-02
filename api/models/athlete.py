from django.db import models


class Athlete(models.Model):
    name = models.TextField(max_length=255,
                            verbose_name='Nome do Atleta',
                            null=True
                            )
    athlete_code = models.TextField(max_length=255,
                                    verbose_name='Id do Atleta',
                                    null=True
                                    )
    birth_date = models.DateField(verbose_name='Nascimento',
                                  null=True
                                  )
    club = models.TextField(max_length=255,
                            verbose_name='Clube',
                            null=True
                            )

    class Meta:
        verbose_name = 'Atleta'

    def __str__(self):
        return self.name
