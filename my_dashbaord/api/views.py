from rest_framework import viewsets
from .models import User, UsersList
from.serializers import UserSerializer, UsersListSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UsersListView(viewsets.ModelViewSet):
    queryset = UsersList.objects.all()
    serializer_class = UsersListSerializer