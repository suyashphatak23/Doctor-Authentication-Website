from django import forms

from .models import Contact, SuperAdmin


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name', 'email', 'suggestion'
        ]


class SuperAdminForm(forms.ModelForm):
    class Meta:
        model = SuperAdmin
        fields = [
            'name', 'permission', 'aadhar'
        ]
