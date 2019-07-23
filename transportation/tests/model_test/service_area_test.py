from django.test import TestCase
from transportation.models import Provider, ServiceArea


class ServiceAreaModelTestCase(TestCase):
    """This class defines the tests suite for the Serivce Area model_test."""

    def setUp(self):
        """Define the tests client and other tests variables."""
        self.provider_name = "Company ABC"
        self.provider_email = "services@companyabc.com"
        self.provider_phone = "+11231231234"
        self.provider_language = "ENG"
        self.provider_curreny = "USD"
        self.provider = Provider(name=self.provider_name,
                                 email=self.provider_email,
                                 phone=self.provider_phone,
                                 language=self.provider_language,
                                 currency=self.provider_curreny, )
        self.provider.save()

        self.service_area_name = "Route A"
        self.service_area_price = 2.50
        self.service_area_geojson = "{}"

    def test_create_a_service_area_will_pass(self):
        """Test the provider model can create a service area."""
        old_count = ServiceArea.objects.count()
        service_area = ServiceArea(name=self.service_area_name,
                                   provider=self.provider,
                                   price=self.service_area_price,
                                   geojson=self.service_area_geojson,)
        service_area.save()
        new_count = ServiceArea.objects.count()
        self.assertNotEqual(old_count, new_count)
        self.assertEqual(new_count, 1)

    def test_create_service_area_without_name_will_fail(self):
        """Test the service area model cannot create a service area without name."""
        try:
            service_area = ServiceArea(name=None,
                                       provider=self.provider,
                                       price=self.service_area_price,
                                       geojson=self.service_area_geojson, )
            service_area.save()
        except:
            self.failureException()

    def test_create_service_area_without_provider_will_fail(self):
        """Test the service area model cannot create a service area without provider."""
        try:
            service_area = ServiceArea(name=self.service_area_name,
                                       provider=None,
                                       price=self.service_area_price,
                                       geojson=self.service_area_geojson, )
            service_area.save()
        except:
            self.failureException()

    def test_create_service_area_without_price_will_fail(self):
        """Test the service area model cannot create a service area without price."""
        try:
            service_area = ServiceArea(name=self.service_area_name,
                                       provider=self.provider,
                                       price=None,
                                       geojson=self.service_area_geojson, )
            service_area.save()
        except:
            self.failureException()

    def test_create_service_area_without_geojson_will_fail(self):
        """Test the service area model cannot create a service area without geojson."""
        try:
            service_area = ServiceArea(name=self.service_area_name,
                                       provider=self.provider,
                                       price=self.service_area_price,
                                       geojson=None, )
            service_area.save()
        except:
            self.failureException()

