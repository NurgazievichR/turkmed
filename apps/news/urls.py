from rest_framework import routers

from apps.news.views import NewsAPIViewSet

router = routers.DefaultRouter()
router.register('', NewsAPIViewSet)

urlpatterns = router.urls