from django.contrib import admin

from polls.models import Question, Driver

admin.site.register(Question)
admin.site.register(Driver)