from django.db import models
from django.utils import timezone
import datetime


def year_choices():
    a = [(r, r) for r in range(1900, datetime.date.today().year+1)]
    return a


def current_year():
    return datetime.date.today().year


# Gender Drop-down
Male = 'Male'
Female = 'Female'
Other = 'Other'
gender_choices = (
    (Male, 'Male'), (Female, 'Female')
)


class Doctor(models.Model):
    registration_number = models.IntegerField(null=False, primary_key=True, unique=True)
    name = models.CharField(max_length=300, null=False)
    location = models.TextField(max_length=600, null=False)
    contact = models.CharField(max_length=10, null=False)
    gender = models.CharField(max_length=6, choices=gender_choices, default=Male, null=False)
    DOB = models.DateField(default=timezone.now, null=False)
    DOR = models.DateField(default=timezone.now, null=False)
    council = models.CharField(max_length=300, null=False, default="I.M.A.")
    fathers_name = models.CharField(max_length=200, null=True)
    qualified_year = models.IntegerField(('year'), choices=list(year_choices()), default=current_year)
    university = models.CharField(max_length=400, null=True)
    max_qualification = models.CharField(max_length=250, null=False, default="M.B.B.S.")
    ratings = models.FloatField(max_length=1, null=False, default=1)
    image = models.ImageField(upload_to='Doctors/', null=False, max_length=300)

    def _str_(self):
        return str(self.registration_number)


class AdditionalInfo(models.Model):
    doctor = models.ForeignKey(Doctor, default=None, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=250, null=True)
    year = models.IntegerField(('year'), choices=list(year_choices()), default=current_year)
    university = models.CharField(max_length=200, null=True)

    def _str_(self):
        return self.qualification
