from django.contrib import admin
from django.contrib.auth.models import User, Group

from apps.doctors.models import Doctor, DoctorAward, HospitalAward
from apps.appointment.models import Appointment

admin.site.unregister(User)
admin.site.unregister(Group)

class DoctorAwardInline(admin.TabularInline):
    model = DoctorAward

class DoctorAppointmentInline(admin.TabularInline):
    model = Appointment


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    inlines = (DoctorAwardInline,DoctorAppointmentInline)

admin.site.register(HospitalAward)



    
