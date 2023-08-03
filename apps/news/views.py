from rest_framework import viewsets

from apps.news.models import New
from apps.news.serializers import NewSerializer

class NewsAPIViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer