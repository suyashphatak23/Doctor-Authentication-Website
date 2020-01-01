from django.db import models
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField(blank=False, max_length=50, null=False)
    email = models.EmailField(blank=False, null=False, max_length=100)
    suggestion = models.TextField(null=False, blank=False,)
    date = models.DateField(default=timezone.now, blank=False, null=True)


class SuperAdmin(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    permission = models.TextField(null=False, blank=False,)
    aadhar = models.IntegerField(null=False, blank=False,)

