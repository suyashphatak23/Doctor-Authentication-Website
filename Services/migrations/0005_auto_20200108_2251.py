# Generated by Django 2.1 on 2020-01-08 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0004_auto_20200108_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='Additional_Qualifications_2_year_2',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='university_2',
            field=models.CharField(default='NA', max_length=200, null=True),
        ),
    ]
