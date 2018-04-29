from django_tables2 import tables, Column
from django_tables2.export import TableExport

from .models import Driver, Testing, Acceleration, Skid_Pad, AutoX, Endurance, Lap_time


class DriverTable(tables.Table):
    class Meta:
        model = Driver
        template_name = 'django_tables2/bootstrap-responsive.html'
        sequence = ('name', 'surname', 'email', 'weight', 'height', 'gender', 'birthday', 'creation')


class TestingTable(tables.Table):
    class Meta:
        model = Testing
        template_name = 'django_tables2/bootstrap-responsive.html'
        sequence = ('id', '...')


class LapTable(tables.Table):

    class Meta:
        model = Lap_time
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = ('id', 'time', 'driver')

class AccelerationTable(tables.Table):
    setup = Column(accessor='params.id', verbose_name='Setup')
    driver = Column(accessor='params.driver')
    driver_ = Column(accessor='params.driver.surname')
    date = Column(accessor='date')
    place = Column(accessor='params.location')

    class Meta:
        model = Acceleration
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = ('id', 'time', 'date', 'setup', 'driver', 'driver_', 'place')
        #sequence = ('id', 'time', 'date', 'setup', 'driver', 'driver_', 'place')



class SkidPadTable(tables.Table):
    setup = Column(accessor='params.id', verbose_name='Setup')
    driver = Column(accessor='params.driver')
    driver_ = Column(accessor='params.driver.surname')
    date = Column(accessor='date')
    place = Column(accessor='params.location')
    time = Column(accessor='time', verbose_name='Total time')

    class Meta:
        model = Skid_Pad
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = ('id','l1_time', 'l2_time', 'r1_time', 'r2_time', 'time', 'date', 'setup', 'driver', 'driver_', 'place')


class AutoXTable(tables.Table):
    setup = Column(accessor='params.id', verbose_name='Setup')
    driver = Column(accessor='params.driver')
    driver_ = Column(accessor='params.driver.surname')
    date = Column(accessor='date')
    place = Column(accessor='params.location')

    class Meta:
        model = AutoX
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = ('id','length_lap', 'time', 'date', 'setup', 'driver', 'driver_', 'place')


class EnduranceTable(tables.Table):
    setup_ini = Column(accessor='setup_ini.id', verbose_name='First Driver Setup')
    setup_mid = Column(accessor='setup_mid.id', verbose_name='Second Driver Setup')
    driver_1 = Column(accessor='setup_ini.driver', verbose_name='First Driver')
    driver_2 = Column(accessor='setup_mid.driver', verbose_name='Second Driver')
    date = Column(accessor='setup_ini.date')
    place = Column(accessor='setup_ini.location')
    total_time = Column(accessor='total_time')

    class Meta:
        model = Endurance
        template_name = 'django_tables2/bootstrap-responsive.html'
