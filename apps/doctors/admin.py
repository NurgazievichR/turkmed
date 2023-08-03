from django.contrib import admin
from django.contrib.auth.models import User, Group

from apps.doctors.models import Doctor

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Doctor)