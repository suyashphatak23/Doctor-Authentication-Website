# Generated by Django 4.0 on 2022-01-30 18:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0011_remove_doctor_ratings'),
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='name',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='publish',
        ),
        migrations.RemoveField(
            model_name='complaint',
            name='reporter',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='name',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='publish',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='ratings',
        ),
        migrations.AddField(
            model_name='complaint',
            name='doctor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Services.doctor'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 31, 0, 1, 42, 166137)),
        ),
        migrations.AddField(
            model_name='feedback',
            name='doctor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Services.doctor'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 31, 0, 1, 42, 166137)),
        ),
    ]
