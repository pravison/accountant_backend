from django.db import models
from accounts.models import ChartsOfAccounts

# Create your models here.

class Transaction(models.Model):
    chartsOfAccounts =  models.CharField(max_length=200, blank=True, null=True)
    debitAmount = models.FloatField(default=0, null=True)
    creditAmount = models.FloatField(default=0, null=True)
    transactionType = models.CharField(max_length=200, blank=True)
    toWhichAccount = models.CharField(max_length=200, blank=True, null=True)
    fromWhichAccount = models.CharField(max_length=200, blank=True, null=True)
    toWho = models.CharField(max_length=500, blank=True, null=True)
    forWhat = models.CharField(max_length=700, blank=True, null=True)
    fromWho = models.CharField(max_length=500, blank=True, null=True)
    costOfGoodSold = models.FloatField(default=0, null=True)
    description = models.TextField(blank=True, null=True)
    paidComplete = models.BooleanField(null=True, default=False)
    date = models.DateField(blank=True, null=True)
    cost = models.FloatField(default=0, null=True)
    interestPaidUpfront = models.BooleanField(blank=True, default=False, null=True)

    def __str__(self):
        return self.chartsOfAccounts

class CapitalWithdrawal(models.Model):
    debitAmount = models.FloatField(default=0)
    cost = models.FloatField(default=0)
    toWho = models.CharField(max_length=300, blank=True)
    fromWhichAccount = models.CharField(blank=True, max_length=200) #choices for sub cass account
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.debitAmount)

class Loan(models.Model):
    amount = models.FloatField()
    totalLoanPayable = models.FloatField() 
    loanBalance = models.FloatField(default=0, null=True)
    installment = models.FloatField()
    extraCost = models.FloatField(default=0, null=True)
    installmentPaymentDuration = models.CharField(max_length=150, blank=True)#choices
    dayTaken = models.DateField(max_length=120)
    paidUntil = models.DateField(max_length=120)
    toWhichAccount = models.CharField(max_length=120) #choices for sub cass account
    fromWho = models.CharField(max_length=200, blank=True) 
    interestPaidUpfront = models.BooleanField(null=True, blank=True) #intrests paid upfront on loans will be treated as prepaid expense
    description = models.TextField(blank=True)

    def __str__(self) :
        return f'{str(self.amount)} taken {self.dayTaken} from {self.fromWho}'
