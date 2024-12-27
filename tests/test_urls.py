from django.test import SimpleTestCase , TestCase , Client
from django.urls import reverse , resolve
from kjapp.views import CLientViewSet , CLientAllDetailsViewSet
from rest_framework import status
import os
import json
import jsonschema
from jsonschema import validate
import logging
json_file_path = os.path.join(os.path.dirname(__file__), 'data.json')


logger = logging.getLogger(__name__)

def load_json_file(json_file_path):
  try:
    with open(json_file_path, 'r') as json_file:
      data = json.load(json_file)
      return data
  except FileNotFoundError:
        print(f"Error: The file {json_file_path} was not found.")
        return None
  except json.JSONDecodeError:
        print(f"Error: The file {json_file_path} contains invalid JSON.")
        return None   



class TestUrls(TestCase):

    def setUp(self):
      self.json_data = load_json_file(json_file_path)
      self.detail_url = reverse('all-detail-list')
      self.diet_plan_url = reverse('client-diet-list')
      self.member_list_url = reverse('member-list-list')
      self.address_url = reverse('address-list')


    def create_client(self):
        """Helper method to create a client."""
        client_data = self.json_data[0].get("details")
        response = self.client.post(self.detail_url, data=client_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, "Client creation failed")
        return response.json().get("id")  # Return the created client's ID

    def test_client_creation(self):
        """Test the client creation endpoint."""
        client_id = self.create_client()  # Ensure the client is created
        self.assertIsNotNone(client_id, "Client ID should not be None")

    def test_diet_plan_creation(self):
        """Test the diet plan creation endpoint (dependent on client)."""
        client_id = self.create_client()
        diet_data = self.json_data[2].get("diet")
        diet_data["client"] = client_id  # Associate the diet plan with the client

        response = self.client.post(self.diet_plan_url, data=diet_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, "Diet plan creation failed")

    def test_member_list_endpoint(self):
        """Test fetching the member list (dependent on client)."""
        self.create_client()  # Ensure a client exists
        response = self.client.get(self.member_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Fetching member list failed")

    def test_address_endpoint(self):
        """Test fetching the address list (dependent on client)."""
        self.create_client()  # Ensure a client exists
        response = self.client.get(self.address_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, "Fetching address list failed")


      










   