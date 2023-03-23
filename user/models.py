from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid
import datetime


class UserManager(BaseUserManager):
    """
    Use to create usermanager for the User model 
    """ 

    def create_user(self, username,  email, password=None, **kwargs):
        if email is None:
            raise TypeError("Email Required!")
        
        if password is None:
            raise TypeError("Password Required!")
        
        if username is None:
            raise TypeError("Username Required!")
        
        user = self.model(username=username, email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, username, email, password=None, **kwargs):

        if email is None:
            raise TypeError("Email Required!")
        
        if password is None:
            raise TypeError("Password Required!")
        
        if username is None:
            raise TypeError("Username Required!")
        
        user = self.create_user(username, email, password, *kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    public_id = models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)
    username = models.CharField(db_index=True, unique=True, max_length=400)
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    email = models.EmailField(db_index=True, unique=True)
    last_seen = models.DateTimeField(default=datetime.datetime.now)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True) 


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"
    

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"