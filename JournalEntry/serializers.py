from rest_framework import serializers
from .models import *


class JournalEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JournalEntry
        fields = ('id', 'url', 'user', 'date', 'description', 'address_2', 'debit_account', 'debit_amount',
                  'credit_account', 'credit_amount')


class AccountEntriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccountEntries
        fields = ('id', 'url', 'name', 'chart_of_account')
