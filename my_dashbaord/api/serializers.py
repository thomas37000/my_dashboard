from rest_framework import serializers
from .models import User, UsersList


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersList
        fields = "__all__"
