from rest_framework import viewsets

from api.controllers import file_get_all
from api.serializers import FileSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = file_get_all()
    serializer_class = FileSerializer
