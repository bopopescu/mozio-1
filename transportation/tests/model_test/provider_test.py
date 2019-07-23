from django.test import TestCase
from transportation.models import Provider


class ProviderModelTestCase(TestCase):
    """This class defines the tests suite for the Provider model_test."""

    def setUp(self):
        """Define the tests client and other tests variables."""
        self.provider_name = "Company ABC"
        self.provider_email = "services@companyabc.com"
        self.provider_phone = "+11231231234"
        self.provider_language = "en"
        self.provider_curreny = "USD"

    def test_create_a_provider_will_pass(self):
        """Test the provider model can create a provider."""
        old_count = Provider.objects.count()
        provider = Provider(name=self.provider_name,
                            email=self.provider_email,
                            phone=self.provider_phone,
                            language=self.provider_language,
                            currency=self.provider_curreny, )
        provider.save()
        new_count = Provider.objects.count()
        self.assertNotEqual(old_count, new_count)
        self.assertEqual(new_count, 1)

    def test_create_provider_without_name_will_fail(self):
        """Test the provider model cannot create a provider without name."""
        try:
            provider = Provider(name=None,
                                email=self.provider_email,
                                phone=self.provider_phone,
                                language=self.provider_language,
                                currency=self.provider_curreny, )
            provider.save()
        except:
            self.failureException()

    def test_create_provider_without_email_will_fail(self):
        """Test the provider model cannot create a provider without email."""
        try:
            provider = Provider(name=self.provider_name,
                                email=None,
                                phone=self.provider_phone,
                                language=self.provider_language,
                                currency=self.provider_curreny, )
            provider.save()
        except:
            self.failureException()

    def test_create_provider_without_phone_will_fail(self):
        """Test the provider model cannot create a provider without phone."""
        try:
            provider = Provider(name=self.provider_name,
                                email=self.provider_email,
                                phone=None,
                                language=self.provider_language,
                                currency=self.provider_curreny, )
            provider.save()
        except:
            self.failureException()

    def test_create_provider_without_language_will_fail(self):
        """Test the provider model cannot create a provider without language."""
        try:
            provider = Provider(name=self.provider_name,
                                email=self.provider_email,
                                phone=self.provider_phone,
                                language=None,
                                currency=self.provider_curreny, )
            provider.save()
        except:
            self.failureException()

    def test_create_provider_without_currency_will_fail(self):
        """Test the provider model cannot create a provider without currency."""
        try:
            provider = Provider(name=self.provider_name,
                                email=self.provider_email,
                                phone=self.provider_phone,
                                language=self.provider_language,
                                currency=None, )
            provider.save()
        except:
            self.failureException()


