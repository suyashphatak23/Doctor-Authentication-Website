# Generated by Django 2.1 on 2020-01-11 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0006_doctor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6, null=True),
        ),
    ]
