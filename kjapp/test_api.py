# import os 

# from django.urls import reverse
# from rest_framework.test import APITestCase
# from rest_framework import status
# from .models import Client

# class ClientTests(APITestCase):
#     def test_create_client(self):
#         url = reverse('client-list')  # URL for the ClientViewSet
#         data = {'name': 'Test Client', 'email': 'test@example.com'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_get_clients(self):
#         url = reverse('client-list')
#         response = self.client.get(url, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)