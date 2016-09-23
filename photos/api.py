from rest_framework.views import APIView

from photos.models import Photo
from photos.serializers import PhotoSerializer, PhotoListSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class PhotoListAPI(ListCreateAPIView):
    queryset = Photo.objects.all()

    """
    Definición dinámica de serializer. Si es un listado (método get) utilza PhotoListSerializer (3 campos)
    Si es una creación (POST) utiliza PhotoSerializer (8 campos)
    """
    def get_serializer_class(self):
        return PhotoSerializer if self.request.method == "POST" else PhotoListSerializer

class PhotoDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer  # Hay que indicarle la clase. No hay que instanciarla