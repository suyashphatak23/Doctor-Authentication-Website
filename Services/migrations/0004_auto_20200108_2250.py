# Generated by Django 2.1 on 2020-01-08 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0003_auto_20200108_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='Additional_Qualifications_2',
            field=models.CharField(default='NA', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='additional_Qualifications_1',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='additional_Qualifications_1_year_1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='university_1',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
