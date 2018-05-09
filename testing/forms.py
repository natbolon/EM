from django import forms
from django.forms import TextInput
from django.utils.dateparse import parse_duration

from .models import Driver, Testing, Acceleration, Skid_Pad, AutoX, Endurance, Results, Lap_time


class DriverForm(forms.ModelForm):
    """
    Model Form related to Driver Model. Allows registering the data associated to a driver.
    """
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
    """
    Model Form related to Testing Model. Allows registering the setup of the vehicle
    during a run, independently of the event.
    """
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
            roll_bar=forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Roll Bar Position'}),
            antiroll_bar=forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Antiroll Bar Position'}),
            comments=forms.TextInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': '...'}
            )
        )

        exclude = ("",)


class ResultsForm(forms.ModelForm):
    """ Model Form related to Results Model. Allows registering the changes incurred in the vehicle
    parameters during a run, independently of the event.
    """
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
    """ Model Form related to Acceleration. Allows registering the time of each run"""
    class Meta:
        model = Acceleration

        exclude = ("length_lap", 'params')

        widgets = dict(
            time=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': 'SS.MMM'}),

        )


class SkForm(ResultsForm):
    """ Model Form related to Skid Pad. Allows registering the four times involved in the Skid Pad event"""
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
    """ Model Form related to Autocross Model. Allows registering the time and length of each lap"""
    class Meta:
        model = AutoX

        exclude = ('',)

        widgets = dict(
            time=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': 'SSSS.MMM'}),
            length_lap=forms.NumberInput(
                attrs={'class': 'form-control col-md-6', 'placeholder': 'Meters'}
            )
        )


class LapTimeForm(ResultsForm):
    """ Registers the time for each lap in an Endurance; Related to Lap_time model"""
    class Meta:
        model = Lap_time

        exclude = ('',)

        widgets = dict(
            time=forms.NumberInput(attrs={'class': 'form-control col-md-6', 'placeholder': 'SSSS.MMM'}),

        )


class Lap(forms.Form):
    """ only used for registering the lap length in the event of Endurance; Model independent"""
    length = forms.DecimalField(min_value=0)
