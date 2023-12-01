from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TransactionSerializer, CapitalWithdrawalSerializer, LoanSerializer
from . models import Transaction, CapitalWithdrawal, Loan
# Create your views here.

class TransactionView(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()

class CapitalWithdrawalView(viewsets.ModelViewSet):
    serializer_class = CapitalWithdrawalSerializer
    queryset = CapitalWithdrawal.objects.all()

class LoanView(viewsets.ModelViewSet):
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()
    
