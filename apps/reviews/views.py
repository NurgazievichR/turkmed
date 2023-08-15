from rest_framework import viewsets

from apps.reviews.models import Review
from apps.reviews.serializers import ReviewSerializer

class ReviewAPIViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer