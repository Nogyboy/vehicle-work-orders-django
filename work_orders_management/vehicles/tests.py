from django.contrib.auth.models import User
from authentication.models import CustomUser
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Vehicle

class VehicleListAPITest(APITestCase):
    def setUp(self):
        # Clear the test database
        Vehicle.objects.all().delete()

        # Test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.customuser = CustomUser.objects.create(user=self.user, is_cliente=True)

        # Create vehicles for the test user
        Vehicle.objects.create(plate='ADAN1230', brand='Toyota', model='Corolla', user=self.user)
        Vehicle.objects.create(plate='CARL1230', brand='Honda', model='Civic', user=self.user)
        # Vehicle.objects.create(plate='BERT1230', brand='Ford', model='Mustang', user=self.user)

    def test_vehicle_list(self):
        print('Testing vehicle list API endpoint...')
        # Log in as the test user
        self.client.force_authenticate(user=self.user)

        # Make the request
        url = reverse('vehicles-client')
        response = self.client.get(url)

        # Check the response status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the correct number of vehicles are returned
        self.assertEqual(len(response.data), 3)

        # Check that the correct vehicles are returned
        self.assertEqual(response.data[0]['plate'], 'ADAN1230')
        self.assertEqual(response.data[1]['plate'], 'CARL1230')
        self.assertEqual(response.data[2]['plate'], 'BERT1230')

        
