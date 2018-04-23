from django import forms
from django.forms import TextInput
from django.utils.dateparse import parse_duration

from .models import Driver, Testing, Acceleration, Skid_Pad, AutoX, Endurance, Results


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
                attrs={'class': 'form-control col-md-6', 'placeholder': 'IN4 Montmeló'}),
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


class ResultsForm(forms.ModelForm):
    class Meta:
        model = Results
        exclude = ("",)

        widgets = dict(
            temp_inv_ini=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': '25.2'}),
            temp_inv_end=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': '25.2'}),
            temp_bat_ini=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': '25.2'}),
            temp_bat_end=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': '25.2'}),
            temp_pneu_FL_ini=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': '25.2'}),
            temp_pneu_FR_ini=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': '25.2'}),
            temp_pneu_RL_ini=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': '25.2'}),
            temp_pneu_RR_ini=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': '25.2'}),
            temp_pneu_FL_end=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': '25.2'}),
            temp_pneu_FR_end=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': '25.2'}),
            temp_pneu_RL_end=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': '25.2'}),
            temp_pneu_RR_end=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': '25.2'}),
            temp_motor_ini=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': '25.2'}),
            temp_motor_end=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': '25.2'}),
            volt_min_ini=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': '5920'}),
            volt_min_end=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': '5230'}),
            comments=forms.TextInput(attrs={'class': 'form-control col-md-6', 'placeholder': '...'})
        )

        abstract = True


class AccForm(ResultsForm):
    class Meta:
        model = Acceleration

        exclude = ('length', 'params')

        widgets = dict(
            time=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': 'SS.MMM'}),

        )


class SkForm(ResultsForm):
    class Meta:
        model = Skid_Pad

        exclude = ('length_lap', 'total_length', 'params')

        widgets = dict(
            l1_time=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': 'SS.MMM'}),
            l2_time=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': 'SS.MMM'}),
            r1_time=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': 'SS.MMM'}),
            r2_time=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': 'SS.MMM'})
        )


class AXForm(ResultsForm):
    class Meta:
        model = AutoX

        exclude = ('',)

        widgets = dict(
            time=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': 'SSSS.MMM'}),
            length_lap=forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Meters'}
            )
        )


class EnForm(ResultsForm):
    class Meta:
        model = Endurance

        exclude = ('total_length',)

        widgets = dict(
            length_lap=forms.TextInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Meters'}
            )
        )
