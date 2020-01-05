from django.contrib import admin
from .models import Doctor
from import_export.admin import ImportExportModelAdmin


@admin.register(Doctor)
class ViewAdmin(ImportExportModelAdmin):
    pass
