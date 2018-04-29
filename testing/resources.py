from import_export import resources
from import_export.fields import Field

from testing.models import Driver, Testing, Acceleration, AutoX, Skid_Pad, Endurance, Lap_time


class DriverResource(resources.ModelResource):
    class Meta:
        model = Driver


class AccelerationResource(resources.ModelResource):
    class Meta:
        model = Acceleration
        widgets = {
            'params.date': {'format': '%d.%m.%Y'},
        }


class AutoXResource(resources.ModelResource):
    class Meta:
        model = AutoX


class SkidPadResource(resources.ModelResource):
    class Meta:
        model = Skid_Pad


class EnduranceResource(resources.ModelResource):
    class Meta:
        model = Endurance

        fields = ('id', 'length_lap', 'number_laps', 'setup_ini',
                  'setup_mid', 'setup_ini.driver', 'setup_mid.driver', 'time_lap', 'setup_ini.date')


class TestingResource(resources.ModelResource):
    class Meta:
        model = Testing


class LapsResource(resources.ModelResource):
    class Meta:
        model = Lap_time
