from django.test import TestCase
from django.contrib.auth.models import User
from .models import Service

class ServiceTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="testuser", password="12345")
        Service.objects.create(name="Service 1", description="Test Service", price=100.00)

    def test_service_creation(self):
        service = Service.objects.get(name="Service 1")
        self.assertEqual(service.description, "Test Service")
        self.assertEqual(service.price, 100.00)
