from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import View
from users.serializers import UserSerializer
from rest_framework.renderers import JSONRenderer


class UserListAPI(View):
    """
    Obtiene los usuarios del sistemas
    El serializador transforma la lista de objetos User a un diccionario de datos en formato JSON
    """
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True) # Serializa todos los objetos que se le pasan (al ser más de
                                                      # uno es necesario poner many=True
        serialized_users = serializer.data  # Lista de diccionarios
        renderer = JSONRenderer()
        json_users = renderer.render(serialized_users) # Transforma la lista de diccionarios a formato JSON
        return HttpResponse(json_users)
