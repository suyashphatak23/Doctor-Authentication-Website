# Generated by Django 4.0.3 on 2022-07-01 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_alter_complaint_datetime_alter_feedback_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 1, 19, 40, 11, 436427)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 1, 19, 40, 11, 435421)),
        ),
    ]
