from rest_framework import viewsets

from apps.news.models import New, License, Gallery
from apps.news.serializers import NewSerializer, LicenseSerializer, GallerySerializer

class NewsAPIViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer

class LicenseAPIViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer

class GalleryAPIViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer