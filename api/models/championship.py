from django.db import models


class Championship(models.Model):
    name = models.TextField(max_length=255,
                           verbose_name='Nome',
                            null=True)
    occurrence_date = models.DateField(verbose_name='Data de Fim do Campeonato',
                                       null=True)

    class Meta:
        verbose_name = 'Campeonato'

    def __str__(self):
        return self.name
