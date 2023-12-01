from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ChartsOfAccountsSerializer
from . models import ChartsOfAccounts
# Create your views here.

class ChartsView(viewsets.ModelViewSet):
    serializer_class = ChartsOfAccountsSerializer
    queryset = ChartsOfAccounts.objects.all()
    
