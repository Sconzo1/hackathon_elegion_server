from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Reference tables

class Task(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(null=True)

    class Meta:
        db_table = 'tasks'
        ordering = ['name']


# Operated models tables

class UserTask(models.Model):
    id_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user', db_column='id_user')
    id_task = models.ForeignKey(Task, on_delete=models.CASCADE, db_column='id_task')
    id_manager = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='manager',
                                   db_column='id_manager')
    date_expired = models.DateTimeField()
    is_done = models.BooleanField(default=False)
    date_done = models.DateTimeField(null=True)
    weight = models.IntegerField(
        default=3,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    class Meta:
        db_table = 'user_tasks'
        ordering = ['date_expired']
