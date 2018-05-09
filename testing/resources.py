from import_export import resources
from import_export.fields import Field

from testing.models import Driver, Testing, Acceleration, AutoX, Skid_Pad, Endurance, Lap_time


class DriverResource(resources.ModelResource):
    class Meta:
        model = Driver


class TestingResource(resources.ModelResource):
    class Meta:
        model = Testing


class LapsResource(resources.ModelResource):
    class Meta:
        model = Lap_time
