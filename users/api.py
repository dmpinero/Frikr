from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404

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

    def post(self, request):
        serializer = UserSerializer(data=request.data) # Pasa el diccionario de datos
        if serializer.is_valid():                      # Validar el serializador
            new_user = serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)        # Devolver datos del usuario creado
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class UserDetailAPI(APIView):
    """
    Obtiene los usuarios del sistemas
    El serializador transforma la lista de objetos User a un diccionario de datos en formato JSON
    """
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)  # Busca el usuario por clave primaria
        serializer = UserSerializer(user)      # Convierte el objeto en un diccionario. Lo almacena en un atributo data

        return Response(serializer.data)

