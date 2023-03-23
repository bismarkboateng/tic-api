from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()

    class Meta:
        model = User 
        fields = ["id", "email", "first_name", "last_name", "password", "date_joined"]
        extra_kwargs = {"password": {"write_only": True}}