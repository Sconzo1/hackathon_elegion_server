# Generated by Django 3.2.7 on 2021-10-01 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id_chat',
            field=models.ForeignKey(db_column='id_chat', on_delete=django.db.models.deletion.CASCADE, to='chats.chat'),
        ),
    ]