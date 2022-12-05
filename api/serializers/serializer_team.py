from rest_framework import serializers

from api.models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id_athlete_1', 'id_athlete_2', 'name')

