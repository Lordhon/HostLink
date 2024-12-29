from django.core.cache import cache
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_redis import get_redis_connection
from hashlib import md5

from .filters import ListingsFilter
from .models import Listings
from .permissions import IsLandlord
from .serializers import List

def generate_cache_key(view_name, query_params):
    params = "&".join(f"{k}={v}" for k, v in sorted(query_params.items()))
    key = f"{view_name}_{md5(params.encode()).hexdigest()}"
    return key

def delete_cache_pattern(pattern):
    redis_conn = get_redis_connection("default")
    keys = redis_conn.scan_iter(pattern)
    for key in keys:
        redis_conn.delete(key)

class ListingsViewSet(ModelViewSet):
    queryset = Listings.objects.all()
    serializer_class = List
    permission_classes = [IsLandlord]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ListingsFilter

