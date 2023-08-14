from rest_framework import routers

from apps.news.views import NewsAPIViewSet, LicenseAPIViewSet, GalleryAPIViewSet

router = routers.DefaultRouter()
router.register('news', NewsAPIViewSet)
router.register('licenses', LicenseAPIViewSet)
router.register('gallery', GalleryAPIViewSet)


urlpatterns = router.urls