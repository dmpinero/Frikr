from rest_framework.viewsets import ModelViewSet

from photos.models import Photo
from photos.serializers import PhotoSerializer, PhotoListSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from photos.views import PhotosQuerySet


class PhotoViewSet(PhotosQuerySet, ModelViewSet):
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)  # Si el usuario no está autenticado no puede crear fotos

    def get_queryset(self):
        """
        Definición dinámica del queryset
        :return:
        """
        return self.get_photos_queryset(self.request)  # Método get_photos_queryset de la clase PhotosQuerySet

    def get_serializer_class(self):
        if self.action == 'list':
            return PhotoListSerializer
        else:
            return PhotoSerializer

    def perform_create(self, serializer):
        """
        Este método se ejecuta antes de guardar la información
        Aquí se pueden realizar cambios en el serializador
        :param serializer:
        :return:
        """
        serializer.save(owner=self.request.user)  # Modificamos el owner del objeto con el usuario autenticado