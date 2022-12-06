import os

from api.models import *
from django.contrib.auth.models import User
from datetime import datetime
from api.models.file import TypeFile
from badmint import settings
from django.test import TestCase
from django.core.files import File as DjangoFile


class FileImporterTestCase(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(password='test', first_name='Test', last_name='User', username='test')
        super().setUp()

    def test_import_athlete_file(self):
        file_path = os.path.join(settings.BASE_DIR, 'api', 'tests', 'utils', 'Arquivo_Atletas.xlsx')
        file_athlete = DjangoFile(open(file_path, mode='rb'), name='Arquivo_Atletas')
        file_obj = File.objects.create(user=self.user, name='athlete_test', timestamp=datetime.now(), file=file_athlete,
                                       type=TypeFile.ATHLETE)

        self.assertEqual(File.objects.filter(id=file_obj.id).count(), 1)

    def test_import_championship_file(self):
        file_path = os.path.join(settings.BASE_DIR, 'api', 'tests', 'utils', 'Arquivo_Campeonato.xlsx')
        file_championship = DjangoFile(open(file_path, mode='rb'), name='Arquivo_Campeonato')
        file_obj = File.objects.create(user=self.user, name='championship_test', timestamp=datetime.now(), file=file_championship,
                                       type=TypeFile.CHAMPIONSHIP)

        self.assertEqual(File.objects.filter(id=file_obj.id).count(), 1)
