from django.db import models


# Create your models here.
class GroupOfChartOfAccount(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Groups of Chart of Accounts'

    def __str__(self):
        return self.name


class ChartOfAccountType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Groups of Chart of Accounts'

    def __str__(self):
        return self.name


class ChartOfAccount(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False)
    code = models.IntegerField(unique=True, blank=False)
    parent_path = models.CharField(max_length=500, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=False)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    group_of_chart_of_account = models.ForeignKey(GroupOfChartOfAccount, on_delete=models.CASCADE, blank=True,
                                                  null=True)
    chart_of_account_type = models.ForeignKey(ChartOfAccountType, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.code) + " - " + self.name
