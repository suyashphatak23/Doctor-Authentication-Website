# Generated by Django 2.1 on 2019-12-30 09:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='degree',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='etime',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='fees',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='stime',
        ),
        migrations.AddField(
            model_name='doctor',
            name='Additionalq1',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='Ay1',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='c2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='collegename',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='council',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='dor',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='fathername',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='infoyear',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='qualifiedyear',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='rno',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='location',
            field=models.TextField(max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
