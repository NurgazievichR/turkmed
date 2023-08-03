from rest_framework import viewsets, mixins

from apps.appointment.models import Appointment
from apps.appointment.serializers import AppointmentSerializer

class AppointmentAPIViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    