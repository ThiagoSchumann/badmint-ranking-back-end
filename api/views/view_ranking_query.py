from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import viewsets

from api.models import RankingClassification
from api.serializers import RankingClassificationSerializer


class RankingClassificationViewset(viewsets.ModelViewSet):
    queryset = RankingClassification.objects.all()
    serializer_class = RankingClassificationSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'ranking', 'athlete1MemberID',
                        'athlete1Name', 'athlete1Age', 'athlete1Club', 'period_date', 'championship', ]
    search_fields = ['category', 'ranking', 'athlete1MemberID',
                     'athlete1Name', 'athlete1Age', 'athlete1Club', 'period_date', 'championship']
