from rest_framework import serializers
from .models import *


class ChartOfAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChartOfAccount
        fields = '__all__'


class GroupOfChartOfAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupOfChartOfAccount
        fields = ('id', 'url', 'name', 'description', 'company')


class ChartOfAccountTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChartOfAccountType
        fields = ('id', 'url', 'name', 'description', 'company')
