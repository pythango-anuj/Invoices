# yourapp/tests/test_views.py
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

class InvoiceAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_invoices(self):
        url = reverse('invoice-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_invoice(self):
        url = reverse('invoice-list-create')
        invoice_data = {
            "customer_name": "John Doe",
            "date": "2024-01-24",
            "invoice_details": [
                {"description": "Banana", "quantity": 10, "unit_price": 100, "price": 1000},
            ]
        }

        response = self.client.post(url, data=invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_invoice(self):
        invoice_id = 3
        url = reverse('invoice-retrieve-update-destroy', args=[invoice_id])
        print(url)
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invoice(self):
        invoice_id = 3
        url = reverse('invoice-retrieve-update-destroy', args=[invoice_id])
        updated_data = {
            "customer_name": "Updated Customer",
            "date": "2024-01-25",
            "invoice_details": [
                {"description": "Updated Banana", "quantity": 5, "unit_price": 50, "price": 250},
            ]
        }

        response = self.client.put(url, data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_invoice(self):
        invoice_id = 3
        url = reverse('invoice-retrieve-update-destroy', args=[invoice_id])
        
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
