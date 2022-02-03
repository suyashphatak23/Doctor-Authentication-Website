from django.db import models
import datetime

class Feedback(models.Model):
	doctor_id = models.IntegerField(null=False)
	feedback = models.CharField(max_length=300, null=False)
	datetime = models.DateTimeField(default=datetime.datetime.now())


class Complaint(models.Model):
	doctor_id = models.IntegerField(null=False)
	complaint = models.CharField(max_length=300, null=False)
	datetime = models.DateTimeField(default=datetime.datetime.now())