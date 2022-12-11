from rest_framework import serializers

from api.models import Category, ClassificationScore


class ClassificationScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassificationScore
        fields = ('team',
                  'championship',
                  'category',
                  'classification',
                  'score',
                  'expiration_date')
