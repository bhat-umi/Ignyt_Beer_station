from django.db import models


import uuid
class Reservations(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email=models.CharField(max_length=10)
    description=models.CharField(max_length=10)
    date=models.CharField(max_length=100)