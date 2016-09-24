from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from users.permissions import UserPermission
from rest_framework.viewsets import ViewSet


class UserViewSet(ViewSet):
    permission_classes = (UserPermission,)  # Aplica los permisos indicados en este módulo

    """
    Obtiene los usuarios del sistemas
    El serializador transforma la lista de objetos User a un diccionario de datos en formato JSON
    """
    def list(self, request):
        self.check_permissions(request)
        paginator = PageNumberPagination()            # Instanciación del paginador
        users = User.objects.all()
        paginator.paginate_queryset(users, request)   # Paginar el queryset
        serializer = UserSerializer(users, many=True) # Serializa todos los objetos que se le pasan (al ser más de
                                                      # uno es necesario poner many=True
        serialized_users = serializer.data            # Lista de diccionarios
        return paginator.get_paginated_response(serialized_users)  # Devolver respuesta paginada

    def create(self, request):
        self.check_permissions(request)
        serializer = UserSerializer(data=request.data) # Pasa el diccionario de datos
        if serializer.is_valid():                      # Validar el serializador
            new_user = serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)        # Devolver datos del usuario creado
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk):
        """
        Obtiene los usuarios del sistemas
        El serializador transforma la lista de objetos User a un diccionario de datos en formato JSON
        """
        self.check_permissions(request)
        user = get_object_or_404(User, pk=pk)  # Busca el usuario por clave primaria
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)      # Convierte el objeto en un diccionario. Lo almacena en un atributo data

        return Response(serializer.data)

    def update(self, request, pk):
        """
        API de actualización de un usuario
        :param request: Petición
        :param pk: identificador del usuario a borrar
        :return: Respuesta de Django REST Framework
        """
        self.check_permissions(request)
        user = get_object_or_404(User, pk=pk)  # Busca el usuario por clave primaria
        self.check_object_permissions(request, user)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        """
        API de borrado de usuarios
        :param request: Petición
        :param pk: identificador del usuario a borrar
        :return:
        """
        self.check_permissions(request)
        user = get_object_or_404(User, pk=pk)  # Busca el usuario por clave primaria
        self.check_object_permissions(request, user)
        user.delete()                          # Borra el usuario de la base de datos

        return Response(status=status.HTTP_204_NO_CONTENT)