from django import forms
from .models import FeeStructure,FeePayment

class FeeStructureForm(forms.ModelForm):
    class Meta:
        model = FeeStructure
        fields = '__all__'

class FeePaymentForm(forms.ModelForm):
    class Meta:
        model = FeePayment
        fields = '__all__'

