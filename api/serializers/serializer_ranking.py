from rest_framework import serializers

from api.models import Ranking


class RankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = ('__all__')



