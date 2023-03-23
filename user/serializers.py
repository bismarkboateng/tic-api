from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="public_id", read_only=True, format="hex")
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)


    class Meta:
        model = User
        fields = [
            "id", "username",
            "first_name", "last_name", 
            "email", "last_seen", 
            "created", "updated"
        ]

        read_only_field = ["is_active", "last_seen"]


class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    
    class Meta:
        model = User 
        fields = [
            "id", "email", "username",
            "first_name", "last_name", "password"
        ]


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)