from django.db import models
from django_mysql.models import JSONField


class ServiceArea(models.Model):
    """This class represents the service area models."""
    name = models.CharField(max_length=255, blank=False, null=False)
    provider = models.ForeignKey("Provider", on_delete=models.CASCADE, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    geojson = JSONField(blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the models instance."""
        return "{}".format(self.name)
