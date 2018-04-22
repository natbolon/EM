from import_export import resources
from testing.models import Driver, Testing, Acceleration, AutoX, Skid_Pad


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

class TestingResource(resources.ModelResource):
    class Meta:
        model = Testing