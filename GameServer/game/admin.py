from django.contrib import admin
from .models import InventoryItem, Player

# Register your models here.
admin.site.register(InventoryItem)
admin.site.register(Player)
