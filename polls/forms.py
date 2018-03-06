from django import forms
from .models import Driver


class DriverForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control col-md-6', 'placeholder': "Name"
               }
    ))
    surname = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control col-md-6', 'placeholder': "Surname"}
    ))
    # email = forms.EmailField(widget=forms.EmailField())
    # birthday = forms.DateField(widget=forms.DateField(input_formats=['%Y-%m-%d']))
    # gender = forms.ChoiceField(widget=forms.ChoiceField())
    # weight = forms.DecimalField(widget=forms.DecimalField)
    # height = forms.DecimalField(widget=forms.DecimalField)

    class Meta:
        model = Driver
        # fields = ['name', 'surname', 'email', 'birthday', 'gender', 'weight', 'height']
        exclude = ("creation",)
