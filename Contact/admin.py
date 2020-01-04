from django.contrib import admin
from .models import Contact, SuperAdmin


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'suggestion')


class SuperAdminAdmin(admin.ModelAdmin):
    list_display = ('name', 'permission', 'aadhar')


admin.site.register(Contact, ContactAdmin)
admin.site.register(SuperAdmin, SuperAdminAdmin)
