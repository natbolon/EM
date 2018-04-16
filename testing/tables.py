from django_tables2 import tables
from .models import Driver, Testing, Acceleration, Skid_Pad, AutoX, Endurance


class DriverTable(tables.Table):
    class Meta:
        model = Driver
        template_name = 'django_tables2/bootstrap-responsive.html'
        sequence = ('name', 'surname', 'email', 'weight', 'height', 'gender', 'birthday', 'creation')


class TestingTable(tables.Table):
    class Meta:
        model = Testing
        template_name = 'django_tables2/bootstrap-responsive.html'


class AccelerationTable(tables.Table):
    class Meta:
        model = Acceleration
        template_name = 'django_tables2/bootstrap-responsive.html'


class SkidPadTable(tables.Table):
    class Meta:
        model = Skid_Pad
        template_name = 'django_tables2/bootstrap-responsive.html'


class AutoXTable(tables.Table):
    class Meta:
        model = AutoX
        template_name = 'django_tables2/bootstrap-responsive.html'


class EnduranceTable(tables.Table):
    class Meta:
        model = Endurance
        template_name = 'django_tables2/bootstrap-responsive.html'
