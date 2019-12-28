# Generated by Django 2.1 on 2019-12-27 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('degree', models.CharField(max_length=250)),
                ('fees', models.IntegerField(null=True)),
                ('ratings', models.FloatField(max_length=1, null=True)),
                ('location', models.TextField(max_length=600)),
                ('contact', models.IntegerField(null=True)),
                ('experience', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=10)),
                ('stime', models.CharField(max_length=100, null=True)),
                ('etime', models.CharField(max_length=100, null=True)),
                ('image', models.FileField(max_length=300, null=True, upload_to='doctors/')),
            ],
        ),
    ]