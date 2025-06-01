from rest_framework import serializers
from .models import GameCurrency

class GameCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = GameCurrency
        fields = '__all__'