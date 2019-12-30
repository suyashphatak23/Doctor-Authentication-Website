from django.contrib import admin
from .models import Doctor


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'rno', 'infoyear', 'ratings', 'location', 'contact', 'gender')


admin.site.register(Doctor, DoctorAdmin)
