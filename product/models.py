from django.db import models
from users.models import Vendor


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)


class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=False, blank=False)
    price = models.IntegerField(default=0, null=False, blank=False)
