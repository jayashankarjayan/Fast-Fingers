# Generated by Django 3.2 on 2021-10-29 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fast_fingers', '0002_gamedata_assinged_input'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamedata',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
