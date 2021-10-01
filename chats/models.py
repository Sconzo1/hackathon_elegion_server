from django.contrib.auth import get_user_model
from django.db import models


# Reference tables

class Chat(models.Model):
    id_from_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='from_user',
                                     db_column='id_from_user')
    id_to_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='to_user',
                                   db_column='id_to_user')

    class Meta:
        db_table = 'chats'


# Operated models tables

class Message(models.Model):
    id_chat = models.ForeignKey(Chat, on_delete=models.CASCADE, db_column='id_chat')
    id_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, db_column='id_user')
    datetime = models.DateTimeField()
    content = models.TextField()

    class Meta:
        db_table = 'messages'
        ordering = ['datetime']
