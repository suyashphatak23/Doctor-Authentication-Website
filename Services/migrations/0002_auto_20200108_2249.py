# Generated by Django 2.1 on 2020-01-08 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='Information_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='registration_number',
            field=models.IntegerField(null=True),
        ),
    ]
