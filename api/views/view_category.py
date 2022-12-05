from rest_framework import viewsets

from api.models import Category
from api.serializers.serializer_category import CategorySerializer


class ViewCategory(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
