from rest_framework import serializers
from .models import *


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'url', 'name', 'company_type', 'address_1', 'address_2', 'city', 'state',
                  'country', 'zip_code', 'phone_number', 'email', 'website', 'tax_id',
                  'industry', 'founding_date', 'revenue', 'number_of_employees', 'company_abrv')
