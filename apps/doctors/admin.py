from django.contrib import admin
from django.contrib.auth.models import User, Group

from apps.doctors.models import Doctor, DoctorAward, HospitalAward

admin.site.unregister(User)
admin.site.unregister(Group)

class DoctorAwardInline(admin.TabularInline):
    model = DoctorAward


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    inlines = (DoctorAwardInline,)

admin.site.register(HospitalAward)



    
