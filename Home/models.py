from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    feedback = models.CharField(max_length=350)
    ratings = models.FloatField(max_length=1)
    publish = models.BooleanField(default=False)


class Complaint(models.Model):
    name = models.CharField(max_length=255)
    reporter = models.CharField(max_length=255)
    complaint = models.CharField(max_length=350)
    date = models.CharField(max_length=50)
    publish = models.BooleanField(default=False)



