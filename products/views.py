import django_filters
from rest_framework import viewsets, permissions, filters
from .models import Product
from .serializers import ProductSerializer

class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    # Filter by stock availability (true/false)
    # "Stock Availability" - interpret as "is in stock"
    in_stock = django_filters.BooleanFilter(method='filter_in_stock')

    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price', 'in_stock']

    def filter_in_stock(self, queryset, name, value):
        if value is True:
            return queryset.filter(stock_quantity__gt=0)
        elif value is False:
            return queryset.filter(stock_quantity=0)
        return queryset

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_date')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'category']
