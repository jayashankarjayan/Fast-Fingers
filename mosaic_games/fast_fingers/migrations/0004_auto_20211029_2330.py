# Generated by Django 3.2 on 2021-10-29 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fast_fingers', '0003_gamedata_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamedata',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='gamedata',
            name='start_time',
            field=models.TimeField(auto_now=True),
        ),
    ]
