from django.contrib import admin
from .models import Doctor, AdditionalInfo


class AdditionalInfoAdmin(admin.StackedInline):
    model = AdditionalInfo


class DoctorAdmin(admin.ModelAdmin):
    inlines = [AdditionalInfoAdmin]
    list_display = ('registration_number', 'name', 'ratings')

    class Meta:
        model = Doctor

admin.site.register(Doctor, DoctorAdmin)

