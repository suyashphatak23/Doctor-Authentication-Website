from django.contrib import admin
from .models import Doctor
from django import forms
from import_export.admin import ImportExportModelAdmin


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'ratings', 'location',
                  'contact', 'gender']

    def clean(self):
        registration_number = self.cleaned_data.get('registration_number')
        if len(registration_number) > 5 and len(registration_number) < 5:
            raise forms.ValidationError("5 Numbers compulsory")

        Information_year = self.cleaned_data.get('Information_year')
        if len(Information_year) > 4 and len(Information_year) < 4:
            raise forms.ValidationError("4 Numbers compulsory")

        qualified_year = self.cleaned_data.get('qualified_year')
        if len(qualified_year) > 4 and len(qualified_year) < 4:
            raise forms.ValidationError("4 Numbers compulsory")

        additional_Qualifications_1_year_1 = self.cleaned_data.get('additional_Qualifications_1_year_1')
        if len(additional_Qualifications_1_year_1) > 4 and len(additional_Qualifications_1_year_1) < 4:
            raise forms.ValidationError("4 Numbers compulsory")

        Additional_Qualifications_2_year_2 = self.cleaned_data.get('Additional_Qualifications_2_year_2')
        if len(Additional_Qualifications_2_year_2) > 4 and len(Additional_Qualifications_2_year_2) < 4:
            raise forms.ValidationError("4 Numbers compulsory")

        contact = self.cleaned_data.get('contact')
        if len(contact) > 10 and len(contact) < 10:
            raise forms.ValidationError("4 Numbers compulsory")

        return self.cleaned_data


@admin.register(Doctor)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['name', 'location', 'contact']
