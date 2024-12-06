import uuid

from django.db import models


#Shop Items are the items that will be in the shop only as IAP.
#Receive Items when we buy from shop will always be game currency i.e. Gems, Coins or combined pack

class GameCurrency(models.Model):
    currencyName = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.currencyName

class ShopItem(models.Model):
    itemID = models.UUIDField(primary_key=True, default =uuid.uuid4(), editable=False)
    itemName = models.CharField(max_length=20)
    itemPriceInCents = models.IntegerField()
    itemsToReceiveAfterIAP= models.ManyToManyField(GameCurrency)
    itemsReceivedAmountAfterIAP = models.JSONField(default = dict)

    def __str__(self):
        return self.itemName


