from django.db import models
from django.utils import timezone

# Gender Drop-down
Male = 'Male'
Female = 'Female'
Other = 'Other'
gender_choices = (
    (Male, 'Male'), (Female, 'Female')
)


class Doctor(models.Model):
    name = models.CharField(max_length=300, null=True)
    ratings = models.FloatField(max_length=1, null=True, default=0)
    location = models.TextField(max_length=600, null=True)
    contact = models.CharField(max_length=10, null=True)
    gender = models.CharField(max_length=6, choices=gender_choices, default=Male, null=True)
    DOB = models.DateField(default=timezone.now, null=True)
    DOR = models.DateField(default=timezone.now, null=True)
    registration_number = models.IntegerField(null=True)
    Information_year = models.IntegerField(null=True)
    council = models.CharField(max_length=300, null=True)
    fathers_name = models.CharField(max_length=200, null=True)
    qualified_year = models.FloatField(max_length=4, null=True)
    University = models.CharField(max_length=400, null=True)
    additional_Qualifications_1 = models.CharField(max_length=250, null=True)
    additional_Qualifications_1_year_1 = models.IntegerField(null=True)
    university_1 = models.CharField(max_length=200, null=True)
    Additional_Qualifications_2 = models.CharField(max_length=250, default='NA', null=True)
    Additional_Qualifications_2_year_2 = models.IntegerField(null=True, default=0)
    university_2 = models.CharField(max_length=200, null=True, default='NA')
    image = models.FileField(upload_to='Doctors/', null=True, max_length=300)