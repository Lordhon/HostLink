from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Human

class RegistrationSerializer(serializers.ModelSerializer):
    user = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    role = serializers.ChoiceField(choices=Human.ROLE_CHOICES, required=True)


    class Meta:
        model = Human
        fields = ['user', 'password', 'role']

    def validate_username(self, value):
        # Проверка на уникальность имени пользователя
        if User.objects.filter(user=value).exists():
            raise serializers.ValidationError("A user with this user already exists.")
        return value

    def create(self, validated_data):
        # Извлекаем данные для User
        user = validated_data['user']
        password = validated_data['password']
        role = validated_data['role']


        # Создаем пользователя
        user = User.objects.create_user(username=user, password=password )

        # Создаем объект Human и связываем его с пользователем
        human = Human.objects.create(user=user, role=role)

        return human



class ViewsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class ViewsHumanSerializer(serializers.ModelSerializer):
    user = ViewsUserSerializer()

    class Meta:
        model = Human
        fields = ['user', 'role']