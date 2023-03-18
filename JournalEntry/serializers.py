from rest_framework import serializers
from .models import *


class JournalEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JournalEntry
        fields = '__all__'


class AccountEntriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccountEntries
        fields = '__all__'
