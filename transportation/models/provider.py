from django.db import models
from phone_field import PhoneField
from languages.fields import LanguageField


class Provider(models.Model):
    """This class represents the provider models."""
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone = PhoneField(blank=False, null=False)
    language = LanguageField(blank=False, null=False)
    currency = models.CharField(max_length=3, blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the models instance."""
        return "{}".format(self.name)
