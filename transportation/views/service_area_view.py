from rest_framework import generics
from transportation.models import ServiceArea
from transportation.serializers import ServiceAreaSerializer, ServiceAreaQuerySerializer

from .helper import coord_in_polygon


class ServiceAreaCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Provider."""
        serializer.save()


class ServiceAreaDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer


class ServiceAreaQueryView(generics.ListAPIView):
    """
    This class take a lat/lng pair as arguments
    and return a list of service area that include the given lat/lng.
    """
    serializer_class = ServiceAreaQuerySerializer

    def get_queryset(self, *args, **kwargs):
        if self.request.GET.get('lat') and self.request.GET.get('lng'):
            query_lat = float(self.request.GET.get('lat'))
            query_lng = float(self.request.GET.get('lng'))

            result_list = []
            queryset_list = ServiceArea.objects.all()
            for service_area in queryset_list:
                js = service_area.geojson
                if coord_in_polygon([query_lng, query_lat], js):
                    result_list.append(service_area)
            return result_list
        return None
