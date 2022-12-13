from rest_framework import serializers

from api.models import Category, ClassificationScore, Championship, Team, Athlete


class ChampionshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Championship
        fields = ('name', 'occurrence_date')


class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = ('name', 'athlete_code', 'birth_date', 'club')


class TeamSerializer(serializers.ModelSerializer):
    athlete_1 = AthleteSerializer(many=False)
    athlete_2 = AthleteSerializer(many=False)

    class Meta:
        model = Team
        fields = ('athlete_1', 'athlete_2', 'category', 'name')


class ClassificationScoreSerializer(serializers.ModelSerializer):
    championship = ChampionshipSerializer(many=False)
    team = TeamSerializer(many=False)

    class Meta:
        model = ClassificationScore
        fields = ('team',
                  'championship',
                  'category',
                  'classification',
                  'score',
                  'expiration_date')

    def create(self, validated_data):
        self.championship_name = Championship.objects.get(id=self.championship.id)
