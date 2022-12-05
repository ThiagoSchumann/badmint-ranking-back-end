from rest_framework import viewsets

from api.models import Ranking
from api.serializers import RankingSerializer


class ViewRanking(viewsets.ModelViewSet):
    queryset = Ranking.objects.all()
    serializer_class = RankingSerializer
