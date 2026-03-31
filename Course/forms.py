from django import forms
from .models import Subject,Enrollment

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'