from django_tables2 import tables
from .models import Driver, Testing


class DriverTable(tables.Table):
    class Meta:
        model = Driver
        template_name = 'django_tables2/bootstrap-responsive.html'
        sequence = ('name', 'surname', 'email', 'weight', 'height', 'gender', 'birthday', 'creation')


class TestingTable(tables.Table):
    class Meta:
        model = Testing
        template_name = 'django_tables2/bootstrap-responsive.html'
