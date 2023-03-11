from django.db import models
from django.contrib.auth.models import User
from Accounting.models import ChartOfAccount


# Create your models here.

class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.CharField(max_length=100)
    debit_account = models.ForeignKey('AccountEntries', related_name='debit_entries', on_delete=models.CASCADE)
    debit_amount = models.DecimalField(max_digits=10, decimal_places=2)
    credit_account = models.ForeignKey('AccountEntries', related_name='credit_entries', on_delete=models.CASCADE)
    credit_amount = models.DecimalField(max_digits=10, decimal_places=2)


class AccountEntries(models.Model):
    name = models.CharField(max_length=100)
    chart_of_account = models.ForeignKey('ChartOfAccount', on_delete=models.CASCADE)
