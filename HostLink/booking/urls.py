from django.urls import path
from .views import BookingCreateView, BookingListView, BookingCancelView



urlpatterns = [
    path('create/', BookingCreateView.as_view(), name='create-booking'),
    path('list/', BookingListView.as_view(), name='list-bookings'),
    path('cancel/<int:booking_id>', BookingCancelView.as_view(), name='cancel-booking'),
]