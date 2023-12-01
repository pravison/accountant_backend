from rest_framework import serializers

from .models import ChartsOfAccounts
class ChartsOfAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartsOfAccounts
        fields = '__all__'

