from django import forms
from .models import Feedback, Complaint


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['doctor', 'feedback', 'date']


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['doctor', 'complaint', 'date']
