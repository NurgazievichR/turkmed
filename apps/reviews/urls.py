from rest_framework import routers

from apps.reviews.views import ReviewAPIViewSet

router = routers.DefaultRouter()
router.register('', ReviewAPIViewSet)

urlpatterns = router.urls


