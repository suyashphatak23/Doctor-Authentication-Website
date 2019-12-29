from django import forms
from .models import Feedback, Complaint


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'name',
            'feedback',
            'ratings',
        ]


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = [
            'name',
            'reporter',
            'complaint',
            'date'
        ]