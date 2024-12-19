from django.db import models
from django.contrib.auth.models import User

class Human(models.Model):
    objects = None
    DoesNotExist = None
    ROLE_CHOICES = [
        ('landlord', 'Арендодатель'),
        ('tenant', 'Съемщик'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Один к одному
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)


    def is_landlord(self):
        return self.role == 'landlord'

    def is_tenant(self):
        return self.role == 'tenant'