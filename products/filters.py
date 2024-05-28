import django_filters
from django_filters import FilterSet
from products.models import Product

class ProductListFilter(FilterSet):
    category_ids = django_filters.CharFilter(method='filter_category_ids')
    manufacturer_ids = django_filters.CharFilter(method='filter_manufacturer_ids')

    class Meta:
        model = Product
        fields = {
            'price': ['gte', 'lte']
        }

    def filter_category_ids(self, queryset, name, value):
        return queryset.filter(category__id__in=value.split(','))

    def filter_manufacturer_ids(self, queryset, name, value):
        return queryset.filter(manufacturer__id__in=value.split(','))