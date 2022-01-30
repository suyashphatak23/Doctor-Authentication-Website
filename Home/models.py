from django.db import models
from Services.models import Doctor
from datetime import datetime


class Feedback(models.Model):
    doctor = models.ForeignKey(Doctor, default=None, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=350)
    date = models.DateTimeField(default=datetime.now())


class Complaint(models.Model):
    doctor = models.ForeignKey(Doctor, default=None, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=350)
    date = models.DateTimeField(default=datetime.now())



