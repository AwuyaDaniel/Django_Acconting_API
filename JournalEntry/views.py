from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *


# Create your views here.

class JournalEntryView(viewsets.ModelViewSet):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer


class AccountEntriesView(viewsets.ModelViewSet):
    queryset = AccountEntries.objects.all()
    serializer_class = AccountEntriesSerializer
