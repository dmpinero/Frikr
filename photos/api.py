from rest_framework.views import APIView

from photos.models import Photo
from photos.serializers import PhotoSerializer, PhotoListSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from photos.views import PhotosQuerySet


class PhotoListAPI(PhotosQuerySet, ListCreateAPIView):
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)  # Si el usuario no está autenticado no puede crear fotos

    def get_serializer_class(self):
        """
        Definición dinámica de serializer. Si es un listado (método get) utilza PhotoListSerializer (3 campos)
        Si es una creación (POST) utiliza PhotoSerializer (8 campos)
        :return: PhotoSerializer si el método es POST y PhotoListSerializer en otro caso
        """
        return PhotoSerializer if self.request.method == "POST" else PhotoListSerializer

    def get_queryset(self):
        """
        Definición dinámica del queryset
        :return:
        """
        return self.get_photos_queryset(self.request)       # Método get_photos_queryset de la clase PhotosQuerySet

    def perform_create(self, serializer):
        """
        Este método se ejecuta antes de guardar la información
        Aquí se pueden realizar cambios en el serializador
        :param serializer:
        :return:
        """
        serializer.save(owner=self.request.user)  # Modificamos el owner del objeto con el usuario autenticado

class PhotoDetailAPI(PhotosQuerySet, RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer  # Hay que indicarle la clase. No hay que instanciarla
    permission_classes = (IsAuthenticatedOrReadOnly,)  # Si el usuario no está autenticado no puede crear fotos

    def get_queryset(self):
        """
        Definición dinámica del queryset
        :return:
        """
        return self.get_photos_queryset(self.request)  # Método get_photos_queryset de la clase PhotosQuerySet