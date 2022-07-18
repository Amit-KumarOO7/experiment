from pyexpat import model
from django import forms
from .models import CSR, Request

class CSRForm(forms.ModelForm):
    class Meta:
        model = CSR
        fields = "__all__"

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        exclude = ['certificate']

