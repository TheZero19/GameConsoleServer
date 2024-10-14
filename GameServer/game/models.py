from configparser import MAX_INTERPOLATION_DEPTH
from django.db import models
import uuid

# Create your models here.

class InventoryItem(models.Model):
    itemID = models.AutoField(primary_key=True)
    itemName = models.CharField(max_length=30, unique=True)
    itemDescription = models.TextField(max_length=150)
    itemAmount = models.IntegerField()
    is_ownable_unlimited = models.BooleanField()


class Player(models.Model):
    player_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    playerName = models.CharField(max_length=30, unique=False)
    inventory = models.ManyToManyField(InventoryItem)
