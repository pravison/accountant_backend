from django.db import models

# Create your models here.

class Inventory(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(blank=True, max_length=100) 
    inventoryType = models.CharField(blank=True, max_length=200)
    purchasePrice =   models.FloatField(default=0.0)
    ActualPurchasePrice =   models.FloatField(default=0.0)
    quantity = models.FloatField(default=0.0)
    measurementUnit = models.CharField(blank=True, max_length=150) 
    discountReceived =  models.FloatField( default=0.0)
    salePrice =  models.FloatField( default=0.0)
    ActualSalePrice =  models.FloatField( default=0.0)
    discountGiven =  models.FloatField( default=0.0)
    expectedLifespan = models.FloatField( default=0.0)
    currentValue =  models.FloatField(default=0.0)
    monthlyFees =  models.FloatField(default=0.0)
    discarded = models.BooleanField(default=False)
    description = models.TextField(blank=True,) 
    forSale = models.BooleanField( null=True)
    leased = models.BooleanField( null=True)
    date = models.DateField( null=True)

    def __str__(self):
        return self.name

class SoldProduct(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(blank=True, max_length=100) 
    quantity = models.FloatField(default=0.0)
    totalAmount = models.FloatField(default=0.0)
    date = models.DateField( null=True)

    def __str__(self):
        return f'{self.name} {self.quantity} {self.totalAmount}'
        