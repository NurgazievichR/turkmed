from rest_framework import serializers

from apps.doctors.models import Doctor, DoctorAward
from apps.appointment.models import AppointmentTime

class DoctorAwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAward
        fields = ['image']

class AppointmentTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppointmentTime
        fields = ['time', 'appointment', 'isAvailable']



class DoctorSerializer(serializers.ModelSerializer):
    doctor_awards = DoctorAwardSerializer(many=True, read_only=True)
    doctor_appointment_time = AppointmentTimeSerializer(many=True, read_only=True)
    class Meta: 
        model = Doctor
        fields = '__all__'


