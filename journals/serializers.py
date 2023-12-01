from rest_framework import serializers

from .models import Transaction, CapitalWithdrawal, Loan

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class CapitalWithdrawalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapitalWithdrawal
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'