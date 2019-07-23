from rest_framework import generics
from transportation.models import Provider
from transportation.serializers import ProviderSerializer


class ProviderCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Provider."""
        serializer.save()


class ProviderDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
