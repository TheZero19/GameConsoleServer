from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def get_player_profile_by_email(request):

    data = request.body
    user = User.objects.get(email="testEmail@test.test")
    print("=====================USER IS================", user)

@api_view(['POST'])
def create_player_profile_by_email_password(request):
    username = "testUser"
    email = "testEmail@test.test"
    password = "testPassword321!!!"
    newUser = User.objects.create_user(username=username, email=email, password=password)
    newUser.save()
