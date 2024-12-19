
from django.urls import path, include
from rest_framework.generics import DestroyAPIView

from rest_framework.routers import DefaultRouter

from advertisements.views import ListingsViewSet

router = DefaultRouter()
router.register(r'listings', ListingsViewSet)
urlpatterns = [




]+router.urls
urlpatterns += router.urls