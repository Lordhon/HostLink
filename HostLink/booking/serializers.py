from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Listings
from .models import Human, BookingBD


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.user.username')
    listing = serializers.ReadOnlyField(source='listing.title')
    status = serializers.ReadOnlyField(source='listing.status')  # Статус берется из Listings

    class Meta:
        model = BookingBD
        fields = ['id', 'listing', 'user', 'booking_date', 'status', 'updated_at']
