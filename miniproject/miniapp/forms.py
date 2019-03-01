from django import forms
from .models import TeacherModel


class NewTeacherForm(forms.ModelForm):
    class Meta():
        model = TeacherModel
        exclude = ['date_of_entry']
