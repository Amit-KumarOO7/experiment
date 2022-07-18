from pyexpat import model
from django import forms 
from .models import Rootcaim

class RootcaimForm(forms.ModelForm):
    class Meta:
        model = Rootcaim
        exclude = ['certificate']