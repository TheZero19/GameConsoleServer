from django.urls import path
from .views import create_player_profile_by_email_password
from .views import get_player_profile_by_email

urlpatterns = [
    path('create_profile/', create_player_profile_by_email_password),
    path('get_profile_by_email/<str:email>/', get_player_profile_by_email),
]
