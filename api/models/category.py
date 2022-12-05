from django.db import models


class Category(models.Model):
    name = models.TextField(max_length=255,
                            verbose_name='Nome da Categoria',
                            null=True)
    age = models.IntegerField(verbose_name='Idade de Corte',
                              null=True)
    genre = models.TextField(max_length=255,
                             verbose_name='Genero',
                             null=True)
    class Meta:
        verbose_name = 'Categoria'

    def __str__(self):
        return self.name
