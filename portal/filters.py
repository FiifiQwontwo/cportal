import django_filters
from .models import *
from django_filters import DateFilter, CharFilter


class Memberfilter(django_filters.FilterSet):

    name = CharFilter(field_name='last_name', lookup_expr='icontains')
    # start_date = DateFilter(field_name='created_at', lookup_expr='gte')
    # end_date = DateFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Members
        fields = 'chapel', 'group'
        exclude = ['last_name', 'first_name', 'created_at', 'updated_at']
