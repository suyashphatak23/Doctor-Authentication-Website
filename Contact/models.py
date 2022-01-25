from django.db import models


class Contact(models.Model):
    fname = models.CharField(max_length=20, default="")
    lname = models.CharField(max_length=20, default="")
    phone = models.CharField(max_length=10, default="")
    email = models.EmailField(max_length=50, default="")
    message = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.fname + self.lname
