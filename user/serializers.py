from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    last_seen = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = [
            "id", "email",
            "first_name", "last_name",
            "password", "last_seen", "is_active",
        ]

        extra_kwargs = {"password" : {"write_only": True}}