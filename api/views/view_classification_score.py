from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import viewsets

from api.models import ClassificationScore
from api.serializers import ClassificationScoreSerializer


class ClassificationScoreViewset(viewsets.ModelViewSet):
    queryset = ClassificationScore.objects.all()
    serializer_class = ClassificationScoreSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['team',
                        'championship',
                        'category',
                        'classification',
                        'score',
                        'expiration_date',
                        ]
    search_fields = ['team',
                     'championship',
                     'category',
                     'classification',
                     'score',
                     'expiration_date',
                     ]
