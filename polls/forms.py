from django import forms
from .models import Driver


class DriverForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control col-md-6', 'placeholder': "Name"
               }
    ))

    class Meta:
        model = Driver
        # fields = ['name', 'surname', 'email', 'birthday', 'gender', 'weight', 'height']
        exclude = ("creation",)
