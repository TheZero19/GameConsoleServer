from django.urls import path

from .views import get_all_Crr_Types

urlpatterns = [
    path('currencyTypes/', get_all_Crr_Types)
]
