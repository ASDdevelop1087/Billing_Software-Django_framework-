import uuid
from django.db import models

# Create your models here.


class Categorie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    id = models.UUIDField(primary_key=True, editable=False)


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Categorie, on_delete=models.CASCADE, null=True, blank=True, related_name='products')
    description = models.TextField(null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.FloatField()
