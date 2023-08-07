from rest_framework import serializers

from apps.doctors.models import Doctor, DoctorAward

class DoctorAwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAward
        fields = ['image']



class DoctorSerializer(serializers.ModelSerializer):
    doctor_awards = DoctorAwardSerializer(many=True, read_only=True)
    class Meta: 
        model = Doctor
        fields = '__all__'


