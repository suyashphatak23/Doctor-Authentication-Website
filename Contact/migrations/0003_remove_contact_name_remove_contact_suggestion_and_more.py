# Generated by Django 4.0 on 2022-01-24 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0002_delete_superadmin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='suggestion',
        ),
        migrations.AddField(
            model_name='contact',
            name='fname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='contact',
            name='lname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='', max_length=50),
        ),
    ]
