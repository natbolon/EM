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
            'birthday': forms.DateInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': "YYYY-MM-DD"}
            ),
            'gender': forms.Select(
                attrs={'class': 'form-control col-md-6', 'placeholder': "Male"}
            ),
            'weight': forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': "70.0"}
            ),
            'height': forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': "170"}
            )
        }


class NewTestingForm(forms.ModelForm):
    class Meta:
        model = Testing
        # drivers = Driver.objects.all()
        widgets = {
            # 'driver': forms.ModelMultipleChoiceField(queryset=drivers, to_field_name='name'
            #                                         ),
            'location': forms.TextInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'IN4 Montmelo'}
            )
        }
        exclude = ("",)
