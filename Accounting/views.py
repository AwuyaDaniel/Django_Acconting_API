from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


# Create your views here.
class ChartOfAccountView(viewsets.ModelViewSet):
    queryset = ChartOfAccount.objects.all()
    serializer_class = ChartOfAccountSerializer


class GroupOfChartOfAccountView(viewsets.ModelViewSet):
    queryset = GroupOfChartOfAccount.objects.all()
    serializer_class = GroupOfChartOfAccountSerializer


class ChartOfAccountTypeView(viewsets.ModelViewSet):
    queryset = ChartOfAccountType.objects.all()
    serializer_class = ChartOfAccountTypeSerializer
