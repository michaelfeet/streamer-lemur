# Generated by Django 4.1 on 2022-09-04 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_journal'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='media',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.media'),
            preserve_default=False,
        ),
    ]
