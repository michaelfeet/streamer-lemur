# Generated by Django 4.0.6 on 2022-09-08 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_rename_action_media_action_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='action_genre',
        ),
    ]
