from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from authentication.managers import UserManager


class UserType(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'user_types'
        ordering = ['name']


class UserRank(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'user_ranks'
        ordering = ['name']


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=300)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True)
    id_user_type = models.ForeignKey(UserType, models.CASCADE, db_column='id_user_type')
    id_user_rank = models.ForeignKey(UserRank, models.CASCADE, db_column='id_user_rank')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'users'
        ordering = ['email']
