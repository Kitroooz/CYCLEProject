import uuid
from django.contrib.auth.models import User

from django.db import models


# Create your models here.
class Buyer(models.Model):
    objects = None
    Name = models.CharField(max_length=30, blank=True, default=True)
    Surname = models.CharField(max_length=30, blank=True, default=True)

    def __str__(self):
        return f"{self.Name} {self.Surname}"


class Seller(models.Model):
    objects = None
    Name = models.CharField(max_length=30, blank=True, default=True)
    Surname = models.CharField(max_length=30, blank=True, default=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Name} {self.Surname}"


class Item(models.Model):
    code = models.UUIDField(primary_key=True, default=uuid.uuid4)
    image = models.ImageField(upload_to='static/')
    name = models.CharField(max_length=30, blank=True, default=True)
    manufacturer = models.CharField(max_length=30, blank=False, default=True)
    description = models.TextField(max_length=1000, blank=False, default=True)
    price = models.IntegerField(blank=False, default=True)
    stock = models.IntegerField(blank=False, default=True)
    type = models.CharField(max_length=30, blank=True, default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class BuyerItem(models.Model):
    Buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    Item = models.ForeignKey(Item, on_delete=models.CASCADE)
