from django.contrib import admin
from .models import Feedback, Complaint


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'feedback')


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'complaint')


admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Complaint, ComplaintAdmin)

