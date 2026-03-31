from django import forms
from .models import Exam,Result

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = '__all__'