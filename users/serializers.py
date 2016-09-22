from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.Serializer):

    # Atributos a devolver
    id = serializers.ReadOnlyField()  # Atributo de sólo lectura
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        """
        Crea una instancia de User a poartir de los datos de
        validated_data que contiene valores deserializados
        :param validated_data: Diccionario con los datos de usuario
        :return: objeto User
        """
        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        """
        Actualiza una instancia de User a poartir de los datos de
        validated_data que contiene valores deserializados
        :param validated_data: Diccionario con los datos de usuario
        :return: objeto User
        """
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.set_password(validated_data.get('password'))  # La constraseña hay que encriptarla
        instance.save()  # Guardar objeto en la base de datos

        return instance