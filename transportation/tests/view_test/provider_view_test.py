from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from transportation.models import Provider


class ProviderViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the tests client and other tests variables."""
        self.client = APIClient()
        self.provider_data = {"name": "ABC Company",
                              "email": "services@abccompany.com",
                              "phone": "+11231231234",
                              "language": "en",
                              "currency": "USD", }
        self.response = self.client.post(reverse('provider_create'),
                                         self.provider_data,
                                         format="json")

    def test_api_create_a_provider_will_pass(self):
        """Test the api has provider creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_get_a_provider_will_pass(self):
        """Test the api can get a given provider."""
        provider = Provider.objects.get()
        response = self.client.get(reverse('provider_details', kwargs={'pk': provider.id}),
                                   format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, provider)

    def test_api_update_provider_will_pass(self):
        """Test the api can update a given provider."""
        provider = Provider.objects.get()
        change_provider = {"name": "XYZ Company",
                           "email": "services@abccompany.com",
                           "phone": "+11231231234",
                           "language": "en",
                           "currency": "USD", }
        res = self.client.put(reverse('provider_details', kwargs={'pk': provider.id}),
                              change_provider,
                              format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_delete_provider_will_pass(self):
        """Test the api can delete a provider."""
        provider = Provider.objects.get()
        response = self.client.delete(reverse('provider_details', kwargs={'pk': provider.id}),
                                      format='json',
                                      follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
