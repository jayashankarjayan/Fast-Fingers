# Generated by Django 3.2 on 2021-10-29 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fast_fingers', '0004_auto_20211029_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamedata',
            name='start_time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]
