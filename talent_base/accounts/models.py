from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .manager import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):     #Creating the custom model where user's email id is the key
    email=models.EmailField(unique=True)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    
    objects=CustomUserManager()