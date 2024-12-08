from django.urls import path

from .views import get_all_Crr_Types

urlpatterns = [
    path('', get_all_Crr_Types)
]
