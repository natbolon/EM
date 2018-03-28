from django import forms
from django.forms import TextInput
from django.utils.dateparse import parse_duration

from .models import Driver, Testing, Acceleration


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

        widgets = dict(
            driver=forms.Select(
                attrs={'class': 'form-control col-md-6', 'placeholder': "Select driver"}),
            location=forms.TextInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'IN4 Montmelo'}),
            event=forms.Select(),
            mode=forms.NumberInput(
                attrs={'class': 'form-control col-md-6'}),
            cont_current_p=forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Continuous current'}),
            peak_current_p=forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Peak current'}),
            kp_current=forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Peak current'}),
            ti_current=forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Peak current'}),
            kp_speed=forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Peak current'}),
            ti_speed=forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Peak current'}),
            fw_flap1_degrees=forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Front Wing Flap1'}),
            fw_flap2_degrees=forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Front Wing Flap2'}),
            rw_flap1_degrees=forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Rear Wing Flap1'}),
            rw_flap2_degrees=forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Rear Wing Flap2'}),
            drs=forms.CheckboxInput(attrs={}),
            front_camber=forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Front Camber'}),
            rear_camber=forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Rear Camber'}),
            front_toe=forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Front Toe'}),
            rear_toe=forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Rear Toe'}),
            front_pressure=forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Front Pressure'}),
            rear_pressure=forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Rear Pressure'}),
            front_weight=forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Front Weight'}),
            rear_weight=forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Rear Weight'}),
            front_height=forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Front Height'}),
            rear_height=forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Rear Height'}),
            comments=forms.TextInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': '...'}
            )
        )

        exclude = ("",)


class AccForm(forms.ModelForm):
    class Meta:
        model = Acceleration

        exclude = ('length',)

        widgets = dict(
            time=forms.TextInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'SS.MMM'}
            )
        )
