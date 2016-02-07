from django.shortcuts import render
from users.models import User
from users.serializers import UserSerializer
from rest_framework import viewsets


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
