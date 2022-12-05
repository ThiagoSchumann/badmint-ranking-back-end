from rest_framework import serializers
from api.models import RankingClassification


class RankingClassificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = RankingClassification
        fields = ('__all__')
