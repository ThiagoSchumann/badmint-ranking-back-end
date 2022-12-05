from rest_framework import viewsets

from api.models import RankingClassification
from api.serializers import RankingClassificationSerializer


class RankingClassificationViewset(viewsets.ModelViewSet):
    queryset = RankingClassification.objects.all()
    serializer_class = RankingClassificationSerializer
