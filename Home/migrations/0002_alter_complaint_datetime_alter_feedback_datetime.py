# Generated by Django 4.0 on 2022-02-02 17:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 2, 23, 7, 1, 950306)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 2, 23, 7, 1, 950306)),
        ),
    ]
