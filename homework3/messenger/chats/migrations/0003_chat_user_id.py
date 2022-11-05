# Generated by Django 2.2.12 on 2022-11-05 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20221105_1806'),
        ('chats', '0002_remove_chat_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.MyUser', verbose_name='user'),
        ),
    ]