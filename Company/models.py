from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=250)
    company_type = models.CharField(max_length=250)
    address_1 = models.CharField(max_length=250)
    address_2 = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    zip_code = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.CharField(max_length=300)
    tax_id = models.CharField(max_length=300)
    industry = models.CharField(max_length=300)
    founding_date = models.DateField()
    revenue = models.CharField(max_length=300)
    number_of_employees = models.IntegerField()
    company_abrv = models.CharField(max_length=8)





