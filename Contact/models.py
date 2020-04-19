from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    suggestion = models.TextField()


class SuperAdmin(models.Model):
    name = models.CharField(max_length=50)
    permission = models.TextField()
    aadhar = models.IntegerField()