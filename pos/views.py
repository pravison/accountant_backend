from django.shortcuts import render
from rest_framework import viewsets
from .serializers import InventorySerializer, SoldProductSerializer
from . models import Inventory, SoldProduct
# Create your views here.

class InventoryView(viewsets.ModelViewSet):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()

class SoldProductView(viewsets.ModelViewSet):
    serializer_class = SoldProductSerializer
    queryset = SoldProduct.objects.all()
    
