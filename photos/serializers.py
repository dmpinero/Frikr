from rest_framework import serializers
from photos.models import Photo


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        read_only_fields = ('owner')

class PhotoListSerializer(PhotoSerializer):
    """
    Serializador para listado de fotos. Muestra menos campos que en el detalle de la foto
    """
    class Meta(PhotoSerializer.Meta):
        fields = ('id', 'name', 'url')