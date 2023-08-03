from rest_framework import routers 

from apps.appointment.views import AppointmentAPIViewSet

router = routers.DefaultRouter()
router.register('', AppointmentAPIViewSet)

urlpatterns = router.urls
