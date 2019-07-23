from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from transportation.models import Provider, ServiceArea


class ServiceAreaViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the tests client and other tests variables."""
        self.client = APIClient()
        self.provider_name = "Company ABC"
        self.provider_email = "services@companyabc.com"
        self.provider_phone = "+11231231234"
        self.provider_language = "en"
        self.provider_curreny = "USD"
        self.provider = Provider(name=self.provider_name,
                                 email=self.provider_email,
                                 phone=self.provider_phone,
                                 language=self.provider_language,
                                 currency=self.provider_curreny, )
        self.provider.save()

        self.service_area_data = {"name": "Route A",
                                  "provider": self.provider.pk,
                                  "price": 2.50,
                                  "geojson": "{}", }
        self.response = self.client.post(reverse('service_area_create'),
                                         self.service_area_data,
                                         format="json")

    def test_api_create_a_service_area_will_pass(self):
        """Test the api has provider creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_get_a_service_area_will_pass(self):
        """Test the api can get a given service area."""
        service_area = ServiceArea.objects.get()
        response = self.client.get(reverse('service_area_details', kwargs={'pk': service_area.id}),
                                   format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, service_area)

    def test_api_update_service_area_will_pass(self):
        """Test the api can update a given service area."""
        service_area = ServiceArea.objects.get()
        change_service_area = {"name": "Route A",
                               "provider": self.provider.pk,
                               "price": 5.50,
                               "geojson": "{}", }
        res = self.client.put(reverse('service_area_details', kwargs={'pk': service_area.id}),
                              change_service_area,
                              format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_delete_service_area_will_pass(self):
        """Test the api can delete a service area."""
        service_area = ServiceArea.objects.get()
        response = self.client.delete(reverse('service_area_details', kwargs={'pk': service_area.id}),
                                      format='json',
                                      follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_api_query_service_area_will_pass(self):
        """Test the api can query service area with given lat/lng pair"""
        response = self.client.get(reverse('service_area_query'),
                                   format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
