# Generated by Django 3.2.7 on 2021-10-02 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20211002_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип чата',
                'verbose_name_plural': 'Типы чата',
                'db_table': 'chat_types',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='usertask',
            options={'ordering': ['is_done', 'date_expired'], 'verbose_name': 'Задача пользователя', 'verbose_name_plural': 'Задачи пользователя'},
        ),
        migrations.CreateModel(
            name='ForeignChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('tg_link', models.CharField(max_length=300, verbose_name='Telegram')),
                ('id_type', models.ForeignKey(db_column='id_type', on_delete=django.db.models.deletion.CASCADE, to='api.chattype', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Чат',
                'verbose_name_plural': 'Чаты',
                'db_table': 'foreign_chats',
                'ordering': ['name'],
            },
        ),
    ]
