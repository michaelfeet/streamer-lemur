# Generated by Django 4.1 on 2022-09-07 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_journal_completed_watching_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='genre',
        ),
        migrations.AddField(
            model_name='media',
            name='action',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='media',
            name='anime',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='media',
            name='cartoon',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='media',
            name='comedy',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='media',
            name='documentary',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='media',
            name='drama',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='media',
            name='family',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='media',
            name='fantasy',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='media',
            name='horror',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='media',
            name='mystery',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='media',
            name='romance',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='media',
            name='scifi',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='media',
            name='thriller',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='media',
            name='mpaa_rating',
            field=models.CharField(choices=[('G', 'G'), ('P', 'PG'), ('1', 'PG-13'), ('R', 'R'), ('N', 'NC-17'), ('M', 'Mature Audience, Be Advised'), ('O', 'Not Rated')], default='G', max_length=1),
        ),
    ]
