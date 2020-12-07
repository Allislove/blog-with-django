from rest_framework import serializers
from publicaciones.models import Publicacion

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = '__all__'
