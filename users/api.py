from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UserSerializer

class UserListAPI(APIView):
    """
    Obtiene los usuarios del sistemas
    El serializador transforma la lista de objetos User a un diccionario de datos en formato JSON
    """
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True) # Serializa todos los objetos que se le pasan (al ser más de
                                                      # uno es necesario poner many=True
        serialized_users = serializer.data            # Lista de diccionarios
        return Response(serialized_users)
