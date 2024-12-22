import django_filters
from .models import Listings

class ListingsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title contains')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Price >=')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Price <=')
    created_after = django_filters.DateFilter(field_name='created_at', lookup_expr='gte', label='Created after')
    status = django_filters.CharFilter(lookup_expr='icontains', label='Status contains')

    class Meta:
        model = Listings
        fields = ['title', 'price_min', 'price_max', 'created_after', 'status']