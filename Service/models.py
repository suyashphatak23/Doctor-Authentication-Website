from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=300, null=True)
    rno = models.IntegerField(null=True)
    infoyear = models.IntegerField(null=True)
    council = models.CharField(max_length=300, null=True)
    dob = models.DateField(null=True)
    dor = models.DateField(null=True)
    fathername = models.CharField(max_length=200)
    qualifiedyear = models.IntegerField(null=True)
    collegename = models.CharField(max_length=400, null=True)
    Additionalq1 = models.CharField(max_length=250, null=True)
    Ay1 = models.IntegerField(null=True)
    c2 = models.CharField(max_length=200, null=True)
    ratings = models.FloatField(max_length=1, null=True)
    location = models.TextField(max_length=600, null=True)
    contact = models.CharField(max_length=10, null=True)
    gender = models.CharField(max_length=10, null=True)
    image = models.FileField(upload_to='doctors/', null=True, max_length=300)
