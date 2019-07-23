from rest_framework import serializers
from transportation.models import Provider, ServiceArea


class ServiceAreaSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    providers = Provider.objects.all()
    provider = serializers.PrimaryKeyRelatedField(queryset=providers)
    provider_name = serializers.StringRelatedField(source='provider', read_only=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = ServiceArea
        fields = ('id', 'provider', 'provider_name', 'name', 'price', 'geojson', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class ServiceAreaQuerySerializer(serializers.HyperlinkedModelSerializer):
    """Serializer to map the lat/lng pair into JSON format."""
    providers = Provider.objects.all()
    provider = serializers.PrimaryKeyRelatedField(queryset=providers)
    provider_name = serializers.StringRelatedField(source='provider', read_only=True)

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = ServiceArea
        fields = ('id', 'provider', 'provider_name', 'name', 'price')
