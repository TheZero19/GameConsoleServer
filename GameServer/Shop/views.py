from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import GameCurrency
from .serializers import GameCurrencySerializer

# Create your views here.

@api_view(['GET'])
def get_all_Crr_Types(request):
    allCurrencies = GameCurrency.objects.all()
    jsonData = GameCurrencySerializer(allCurrencies, many=True)

    print(jsonData.data)

    return Response(jsonData.data)
