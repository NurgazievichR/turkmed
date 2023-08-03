from rest_framework import viewsets

from apps.doctors.models import Doctor
from apps.doctors.serializers import DoctorSerializer

class DoctorAPIViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer