from django.db import models



class ChampionshipSheetImportation(models.Model):
    importation_date_time = models.DateField(verbose_name='Data de Importação',
                                             null=True)
    file_name = models.TextField(max_length=255,
                                 verbose_name='Nome',
                                 null=True)
    file = models.FileField(verbose_name='Arquivo',
                            null=True)

    class Meta:
        verbose_name = 'Importação de Planilha de Importação'

    def __str__(self):
        return self.file_name
