from rest_framework import serializers
from .models import *


class ChartOfAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChartOfAccount
        fields = ('id', 'url', 'name', 'code', 'parent_path', 'balance', 'description', 'group_of_chart_of_account',
                  'chart_of_account_type', 'company')


class GroupOfChartOfAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupOfChartOfAccount
        fields = ('id', 'url', 'name', 'description', 'company')


class ChartOfAccountTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChartOfAccountType
        fields = ('id', 'url', 'name', 'description', 'company')
