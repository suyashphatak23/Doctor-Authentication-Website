# Generated by Django 2.1 on 2020-01-01 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0002_auto_20200101_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='date',
        ),
    ]
