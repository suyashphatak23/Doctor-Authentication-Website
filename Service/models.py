from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=300)
    degree = models.CharField(max_length=250)
    fees = models.IntegerField(null=True)
    ratings = models.FloatField(max_length=1, null=True)
    location = models.TextField(max_length=600)
    contact = models.IntegerField(null=True)
    experience = models.IntegerField(null=True)
    gender = models.CharField(max_length=10)
    stime = models.CharField(max_length=100, null=True)
    etime = models.CharField(max_length=100, null=True)
    image = models.FileField(upload_to='doctors/', null=True, max_length=300)

