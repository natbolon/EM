from django import forms
from .models import Driver, Testing


class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        # fields = ['name', 'surname', 'email', 'birthday', 'gender', 'weight', 'height']
        exclude = ("creation",)
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': "Name"}),
            'surname': forms.TextInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': "Surname"}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': "Email"}
            ),
            'birthday': forms.DateTimeInput(
                attrs={'class': 'datetime-input', 'placeholder': "YYYY-MM-DD"}
            ),
            'gender': forms.Select(
                attrs={'class': 'form-control col-md-6', 'placeholder': "Male"}
            ),
            'weight': forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': "70"}
            ),
            'height': forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': "170"}
            )
        }


class NewTestingForm(forms.ModelForm):
    class Meta:
        model = Testing

        widgets = {
            'driver': forms.ModelMultipleChoiceField(['Gerard', 'Marc', 'Oriol']),
            'location': forms.TextInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'IN4 Montmelo'}

            ),
            'event': forms.Select(),
            'mode': forms.NumberInput(
                attrs={'class': 'form-control col-md-6'}),
            'cont_current_p': forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Continuous current'}),
            'peak_current_p': forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Peak current'}),
            'kp_current': forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Peak current'}),
            'ti_current': forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Peak current'}),
            'kp_speed': forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Peak current'}),

            'ti_speed': forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Peak current'})

        }
        exclude = ("",)
