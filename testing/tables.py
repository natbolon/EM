from django_tables2 import tables, Column
from django_tables2.export import TableExport

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
        sequence = ('id', '...')


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
    setup = Column(accessor='params.id', verbose_name='Setup')
    driver = Column(accessor='params.driver')
    driver_ = Column(accessor='params.driver.surname')
    date = Column(accessor='params.date')
    place = Column(accessor='params.location')

    class Meta:
        model = Endurance
        template_name = 'django_tables2/bootstrap-responsive.html'
