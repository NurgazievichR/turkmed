from rest_framework import routers

from apps.doctors.views import DoctorAPIViewSet

router = routers.DefaultRouter()
router.register('', DoctorAPIViewSet)


urlpatterns = router.urls