from django.contrib.auth.models import User
from django.core.exceptions import BadRequest
from rest_framework import serializers

from api.models import File


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ('__all__')

   #def save(self, **kwargs):

   #   #try:
   #   #    id = self.validated_data['user']
   #   #    user = User.objects.get(id=id)
   #   #except User.DoesNotExist:
   #   #    raise BadRequest('Usuário inexistente!')
   #   #except :
   #   #    raise BadRequest('Erro ao carregar usuário!')


   #    file = File(
   #                user=self.validated_data['user'],
   #                name=self.validated_data['name'],
   #                base64=None
   #                )


