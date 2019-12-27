from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    Feedback = models.TextField()
    Ratings = models.FloatField(max_length=1)


class Complaint(models.Model):
    name = models.CharField(max_length=255)
    reporter = models.CharField(max_length=255)
    complaint = models.TextField()
    date = models.DateField()



