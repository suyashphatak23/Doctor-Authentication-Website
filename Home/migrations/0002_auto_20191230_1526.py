# Generated by Django 2.1 on 2019-12-30 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='Feedback',
            new_name='feedback',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='Ratings',
            new_name='ratings',
        ),
    ]
