from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Reference tables

class Task(models.Model):
    name = models.CharField('Задача', max_length=200)
    desc = models.TextField('Описание', null=True)

    class Meta:
        db_table = 'tasks'
        ordering = ['name']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.name


# Operated models tables

class UserTask(models.Model):
    id_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user',
                                verbose_name="Пользователь", db_column='id_user')
    id_task = models.ForeignKey(Task, on_delete=models.CASCADE,
                                verbose_name="Задача", db_column='id_task')
    id_manager = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='manager',
                                   verbose_name="Менеджер", db_column='id_manager')
    date_expired = models.DateTimeField('Время окончания')
    is_done = models.BooleanField('Выполнена?', default=False)
    date_done = models.DateTimeField('Время сдачи', null=True)
    weight = models.IntegerField(
        'Вес',
        default=3,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    class Meta:
        db_table = 'user_tasks'
        ordering = ['is_done', 'date_expired']
        verbose_name = 'Задача пользователя'
        verbose_name_plural = 'Задачи пользователя'

    def __str__(self):
        return f"{self.id_user} || {self.id_task}"
