from rest_framework import serializers
from transportation.models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Provider
        fields = ('id', 'name', 'email', 'phone', 'language', 'currency', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
