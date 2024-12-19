from django.db import models
import django_filters
from users.models import Human


class Listings (models.Model):
    title = models.CharField(max_length=255)  # Заголовок объявления
    description = models.TextField()  # Описание объявления
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    updated_at = models.DateTimeField(auto_now=True)  # Дата обновления



    owner = models.ForeignKey(Human, on_delete=models.CASCADE, related_name='ads')

    def __str__(self):
        return self.title


