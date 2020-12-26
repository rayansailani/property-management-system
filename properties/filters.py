import django_filters
from .models import PropertyForSale, PropertyForRent
from django_filters import NumberFilter, CharFilter


class PropertyFilter(django_filters.FilterSet):
    min_price = NumberFilter(field_name='cost_sqft',
                             lookup_expr="gte")
    max_price = NumberFilter(field_name='cost_sqft', lookup_expr="lte")
    address = CharFilter(field_name='address', lookup_expr="icontains")

    class Meta:
        model = PropertyForSale
        fields = '__all__'
        exclude = ['owner', 'no', 'width', 'length', 'description', ]


class PropertyRentFilter(django_filters.FilterSet):
    min_price = NumberFilter(field_name='rent',
                             lookup_expr="gte")
    max_price = NumberFilter(field_name='rent', lookup_expr="lte")
    location = CharFilter(field_name="address", lookup_expr="icontains")

    class Meta:
        model = PropertyForRent
        fields = "__all__"
        exclude = ['image1', 'image2', 'image3', 'image4',
                   'is_occupied', 'property_name', 'owner', 'address', 'description']
