import django_filters
from .models import PropertyForSale
from django_filters import NumberFilter, CharFilter


class PropertyFilter(django_filters.FilterSet):
    min_price = NumberFilter(field_name='cost_sqft', lookup_expr="gte")
    max_price = NumberFilter(field_name='cost_sqft', lookup_expr="lte")

    class Meta:
        model = PropertyForSale
        fields = '__all__'
        exclude = ['owner', 'no', 'width', 'length', ]
