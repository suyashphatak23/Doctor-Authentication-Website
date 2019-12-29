from django.contrib import admin
from .models import Feedback, Complaint


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'feedback', 'ratings')


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('name', 'reporter', 'complaint', 'date')


admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Complaint, ComplaintAdmin)

