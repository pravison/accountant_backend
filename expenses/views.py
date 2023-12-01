from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ExpenseSerializer, PayrolSerializer, PrepaidExpenseSerializer
from . models import Expense, Payrol, PrepaidExpense
# Create your views here.

class ExpenseView(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()

class PayrolView(viewsets.ModelViewSet):
    serializer_class = PayrolSerializer
    queryset = Payrol.objects.all()

class PrepaidExpenseView(viewsets.ModelViewSet):
    serializer_class = PrepaidExpenseSerializer
    queryset = PrepaidExpense.objects.all()
    
