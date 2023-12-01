from rest_framework import serializers

from .models import Expense, PrepaidExpense, Payrol

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class PrepaidExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrepaidExpense
        fields = '__all__'

class PayrolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payrol
        fields = '__all__'