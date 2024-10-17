import pytest
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from product.models.product import Product


@pytest.mark.django_db
class ProductViewSetTestCase(APITestCase):

    def setUp(self):
    
        self.product = Product.objects.create(
            title='Produto ',
            description='Desc do Produto ',
            price=101.5,
            active=True
        )

        self.list_url = reverse('product-list', kwargs={'version': 'v1'})  
        self.detail_url = reverse('product-detail', kwargs={'version': 'v1', 'pk': self.product.id}) 

    def test_retrieve_product(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        

    def test_delete_product(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        assert Product.objects.count() == 0  
