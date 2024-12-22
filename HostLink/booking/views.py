from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from advertisements.models import Listings
from booking.models import BookingBD
from booking.serializers import BookingSerializer


class BookingCreateView(APIView):
    def post(self, request):
        user = request.user.human
        listing_id = request.data.get('listing_id')
        booking_date = request.data.get('booking_date')

        try:
            listing = Listings.objects.get(id=listing_id)
        except Listings.DoesNotExist:
            return Response({"error": "Listing not found"}, status=status.HTTP_404_NOT_FOUND)

        if listing.status == 'booked':
            return Response({"error": "Listing is already booked"}, status=status.HTTP_400_BAD_REQUEST)

        # Создание бронирования
        booking = BookingBD.objects.create(user=user, listing=listing, booking_date=booking_date)

        # Обновление статуса объявления
        listing.status = 'booked'
        listing.save()

        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookingListView(ListAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        user = self.request.user.human
        return BookingBD.objects.filter(user=user)



class BookingCancelView(APIView):
    def put(self, request, booking_id):
        try:
            booking = BookingBD.objects.get(id=booking_id, user=request.user.human)
        except BookingBD.DoesNotExist:
            return Response({"error": "Booking not found or not allowed"}, status=status.HTTP_404_NOT_FOUND)

        # Обновление статуса объявления на "available"
        listing = booking.listing
        listing.status = 'available'
        listing.save()

        # Удаление или логическое завершение бронирования
        booking.delete()

        return Response({"message": "Booking cancelled, listing is now available"}, status=status.HTTP_200_OK)