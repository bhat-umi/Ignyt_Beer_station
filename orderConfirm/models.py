from django.db import models


class Order(models.Model):
    id = models.CharField(primary_key=True, editable=False,max_length=10)
    total = models.CharField(max_length=100)
    items = models.CharField(max_length=1000)
    timestamp=models.CharField(max_length=30)
