import os

from api.models import *
from django.contrib.auth.models import User
from datetime import datetime

from datetime import date
from api.models.file import TypeFile
from badmint import settings
from django.test import TestCase
from django.core.files import File as DjangoFile


class FileImporterTestCase(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(password='test', first_name='Test', last_name='User', username='test')
        super().setUp()

    def import_athlete_file(self, file_name):
        file_path = os.path.join(settings.BASE_DIR, 'api', 'tests', 'utils', file_name)
        file_athlete = DjangoFile(open(file_path, mode='rb'), name=file_name)
        file_obj = File.objects.create(user=self.user, name=file_name, timestamp=datetime.now(), file=file_athlete,
                                       type=TypeFile.ATHLETE)
        return file_obj.id 

    def import_championship_file(self, file_name):
        file_path = os.path.join(settings.BASE_DIR, 'api', 'tests', 'utils', file_name)
        file_championship = DjangoFile(open(file_path, mode='rb'), name=file_name)
        file_obj = File.objects.create(user=self.user, name=file_name, timestamp=datetime.now(), championship_name=file_name,
         file=file_championship, championship_date=date.today(), type=TypeFile.CHAMPIONSHIP)
        return file_obj.id


    def test_athlete_01_file(self):
        file_id = self.import_athlete_file('Arquivo_Atletas.xlsx') 
        self.assertEqual(File.objects.filter(id=file_id).count(), 1)

    def test_championship_01_file(self):
        file_id = self.import_championship_file('Arquivo_Campeonato.xlsx') 
        self.assertEqual(File.objects.filter(id=file_id).count(), 1)
    
    # algo nesses arquivos está corrompido
    # def test_championship_02_file(self):
    #     file_id = self.import_championship_file('2022_IV_Etapa_final_results_v2.xls') 
    #     self.assertEqual(File.objects.filter(id=file_id).count(), 1)
        
    # def test_championship_03_file(self):
    #     file_id = self.import_championship_file('Final Positions_Joacaba_2022_II_Etapa_v3.xls') 
    #     self.assertEqual(File.objects.filter(id=file_id).count(), 1)

    # def test_championship_04_file(self):
    #     file_id = self.import_championship_file('final_positions_Joacaba_III_2022_v4.xls') 
    #     self.assertEqual(File.objects.filter(id=file_id).count(), 1)
    
    def test_championship_05_file(self):
        file_id = self.import_championship_file('resultados_I_Etapa_2022.xlsx') 
        self.assertEqual(File.objects.filter(id=file_id).count(), 1)
    
    def test_athlete_02_file(self):
        file_id = self.import_athlete_file('Players Campeonato Estadual SC - II Etapa 2022 (Joaçaba).xlsx') 
        self.assertEqual(File.objects.filter(id=file_id).count(), 1)

    def test_athlete_03_file(self):
        file_id = self.import_athlete_file('Players I Etapa Campeonato Estadual (SC) de Badminton 2022 - Blumenau.xlsx') 
        self.assertEqual(File.objects.filter(id=file_id).count(), 1)

    def test_athlete_04_file(self):
        file_id = self.import_athlete_file('Players III Etapa - Campeonato Estadual de Badminton - JoaçabaSC.xlsx') 
        self.assertEqual(File.objects.filter(id=file_id).count(), 1)

    def test_athlete_05_file(self):
        file_id = self.import_athlete_file('Players IV Etapa Campeonato Estadual - ItajaíSC.xlsx') 
        self.assertEqual(File.objects.filter(id=file_id).count(), 1)