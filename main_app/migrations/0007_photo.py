# Generated by Django 4.1 on 2022-09-07 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_journal_where_am_i_watching'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.media')),
            ],
        ),
    ]
