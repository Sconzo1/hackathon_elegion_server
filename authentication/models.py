from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from authentication.managers import UserManager


class UserType(models.Model):
    name = models.CharField('Название', max_length=200)

    class Meta:
        db_table = 'user_types'
        ordering = ['name']
        verbose_name = 'Тип пользователя'
        verbose_name_plural = 'Типы пользователя'

    def __str__(self):
        return self.name


class UserRank(models.Model):
    name = models.CharField('Название', max_length=200)

    class Meta:
        db_table = 'user_ranks'
        ordering = ['name']
        verbose_name = 'Ранг пользователя'
        verbose_name_plural = 'Ранги пользователя'

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Почта', unique=True, max_length=100)
    password = models.CharField('Пароль', max_length=300)
    is_staff = models.BooleanField('Сотрудник?', default=False)
    is_superuser = models.BooleanField('Суперпользователь?', default=False)
    last_login = models.DateTimeField('Время последнего входа', null=True)
    id_user_type = models.ForeignKey(UserType, models.CASCADE, verbose_name='Тип пользователя',
                                     db_column='id_user_type')
    id_user_rank = models.ForeignKey(UserRank, models.CASCADE, verbose_name='Ранг пользователя',
                                     db_column='id_user_rank')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'users'
        ordering = ['email']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
