from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination

class UserListAPI(APIView):
    """
    Obtiene los usuarios del sistemas
    El serializador transforma la lista de objetos User a un diccionario de datos en formato JSON
    """
    def get(self, request):
        paginator = PageNumberPagination()            # Instanciación del paginador
        users = User.objects.all()
        paginator.paginate_queryset(users, request)   # Paginar el queryset
        serializer = UserSerializer(users, many=True) # Serializa todos los objetos que se le pasan (al ser más de
                                                      # uno es necesario poner many=True
        serialized_users = serializer.data            # Lista de diccionarios
        return paginator.get_paginated_response(serialized_users)  # Devolver respuesta paginada

    def post(self, request):
        serializer = UserSerializer(data=request.data) # Pasa el diccionario de datos
        if serializer.is_valid():                      # Validar el serializador
            new_user = serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)        # Devolver datos del usuario creado
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class UserDetailAPI(APIView):
    def get(self, request, pk):
        """
        Obtiene los usuarios del sistemas
        El serializador transforma la lista de objetos User a un diccionario de datos en formato JSON
        """
        user = get_object_or_404(User, pk=pk)  # Busca el usuario por clave primaria
        serializer = UserSerializer(user)      # Convierte el objeto en un diccionario. Lo almacena en un atributo data

        return Response(serializer.data)

    def put(self, request, pk):
        """
        API de actualización de un usuario
        :param request: Petición
        :param pk: identificador del usuario a borrar
        :return: Respuesta de Django REST Framework
        """
        user = get_object_or_404(User, pk=pk)  # Busca el usuario por clave primaria
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        API de borrado de usuarios
        :param request: Petición
        :param pk: identificador del usuario a borrar
        :return:
        """
        user = get_object_or_404(User, pk=pk)  # Busca el usuario por clave primaria
        user.delete()                          # Borra el usuario de la base de datos

        return Response(status=status.HTTP_204_NO_CONTENT)