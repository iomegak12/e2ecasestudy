from django.db import models


class Customer(models.Model):
    customerId = models.CharField(
        max_length=10, primary_key=True)
    customerName = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    credit = models.IntegerField()
    status = models.BooleanField()
    remarks = models.CharField(max_length=1000)
