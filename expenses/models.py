from django.db import models
import datetime

# Create your models here.
class Expense(models.Model):
    expense = models.CharField(max_length=200)
    amount = models.FloatField()
    toWho =models.CharField(max_length=200, blank=True)
    #transactionCost = models.FloatField(default=0)
    #discountReceived = models.FloatField(default=0)
    #fromWhichAccount = models.CharField(max_length=120) #choices for sub cass account
    description = models.TextField(blank=True, max_length=1500)

    def __str__(self):
        return self.expense

class Payrol(models.Model):
    staff = models.CharField(max_length=200)
    amount = models.FloatField(blank=True, default=0)
    commission = models.FloatField(blank=True, default=0)
    AwardsReceived = models.FloatField(blank=True, default=0)
    #fromWhichAccount = models.CharField(max_length=120) #choices for sub cass account
    description = models.TextField(blank=True, max_length=1500)

    def __str__(self):
        return self.staff

class PrepaidExpense(models.Model):
    expense = models.CharField(max_length=200)
    amount = models.FloatField()
    startingDate = models.DateField()
    endingDate = models.DateField()
    fromWhichAccount = models.CharField(max_length=120) #choices for sub cass account
    description = models.TextField(blank=True, max_length=1500)

    def __str__(self):
        return self.expense

