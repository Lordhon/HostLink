from django.db import models

from advertisements.models import Listings
from users.models import Human

class BookingBD (models.Model):

    objects = None
    DoesNotExist = None
    STATUS_CHOICES = [
        ('active', 'active'),
        ('cancelled', 'cancelled'),
    ]


    listing = models.ForeignKey(Listings , on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(Human , on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='cancelled')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking by {self.user.user.username} for {self.listings.title} on {self.booking_date}"