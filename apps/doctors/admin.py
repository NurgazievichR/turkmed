from django.contrib import admin
from django.contrib.auth.models import User, Group

from apps.doctors.models import Doctor, DoctorAward, HospitalAward
from apps.appointment.models import AppointmentTime

admin.site.unregister(User)
admin.site.unregister(Group)

class DoctorAwardInline(admin.TabularInline):
    model = DoctorAward

class AppointmentTimeInline(admin.TabularInline):
    model = AppointmentTime
    fields = ('time','isAvailable')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    inlines = (DoctorAwardInline, AppointmentTimeInline)

admin.site.register(HospitalAward)



    
