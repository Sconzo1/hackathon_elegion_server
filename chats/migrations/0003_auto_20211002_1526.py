# Generated by Django 3.2.7 on 2021-10-02 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0002_alter_message_id_chat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={'verbose_name': 'Чат', 'verbose_name_plural': 'Чаты'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['datetime'], 'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AlterField(
            model_name='chat',
            name='id_from_user',
            field=models.ForeignKey(db_column='id_from_user', on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL, verbose_name='От кого'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='id_to_user',
            field=models.ForeignKey(db_column='id_to_user', on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL, verbose_name='Кому'),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(verbose_name='Тело'),
        ),
        migrations.AlterField(
            model_name='message',
            name='datetime',
            field=models.DateTimeField(verbose_name='Время отправки'),
        ),
        migrations.AlterField(
            model_name='message',
            name='id_chat',
            field=models.ForeignKey(db_column='id_chat', on_delete=django.db.models.deletion.CASCADE, to='chats.chat', verbose_name='Чат'),
        ),
        migrations.AlterField(
            model_name='message',
            name='id_user',
            field=models.ForeignKey(db_column='id_user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
