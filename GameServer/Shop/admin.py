from django.contrib import admin
from .models import ShopItem, GameCurrency

# Register your models here.
admin.site.register(ShopItem)
admin.site.register(GameCurrency)