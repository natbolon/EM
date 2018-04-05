from django.contrib import admin

from testing.models import Driver, Testing, Acceleration, Endurance, SkidPad

admin.site.register(Driver)
admin.site.register(Testing)
admin.site.register(Acceleration)
admin.site.register(Endurance)
admin.site.register(SkidPad)