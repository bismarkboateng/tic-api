from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        db_index=True, unique=True,
        default=uuid.uuid4, editable=False
    )

    username = models.CharField(
        db_index=True, max_length=300, unique=True
        )

    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.EmailField(db_index=True, unique=True)

    profile_pic = models.ImageField(
        upload_to="assets",
        default="assets/profile.png"
        )

    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email}"

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
