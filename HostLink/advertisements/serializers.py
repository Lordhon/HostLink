from django.contrib.auth.models import User
from rest_framework import serializers

from users.models import Human
from .models import Listings

class List(serializers.ModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.user.username')
    status = serializers.CharField()



    class Meta:
        model = Listings
        fields = ['id', 'title', 'description', 'price', 'status' ,  'created_at', 'updated_at', 'owner']
        read_only_fields = ['created_at', 'updated_at', 'owner']

    def create(self, validated_data):
        request = self.context.get('request')
        human = Human.objects.get(user=request.user)
        title = validated_data['title']
        description = validated_data['description']

        price = validated_data['price']
        listing = Listings.objects.create(owner=human, **validated_data)
        return listing





class ListingsListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.user.username')  # Показываем владельца\


    class Meta:
        model = Listings
        fields = ['id', 'title', 'price', 'created_at', 'updated_at', 'owner']


