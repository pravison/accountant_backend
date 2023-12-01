from django.db import models

# Create your models here.
class ChartsOfAccounts(models.Model):
    name = models.CharField(max_length=250)# choices for chart of accounts type
    balance = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name