from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .filters import ListingsFilter
from .models import Human, Listings
from .permissions import IsLandlord
from .serializers import List, ListingsListSerializer


class ListingsViewSet(ModelViewSet):
    queryset = Listings.objects.all()
    serializer_class = List
    permission_classes = [IsAuthenticated , IsLandlord ]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ListingsFilter








