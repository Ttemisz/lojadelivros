import pytest
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from order.models import Order


@pytest.mark.django_db
class OrderViewSetTestCase(APITestCase):

    def setUp(self):
    
        self.order = Order.objects.create(
            email='test@exemplo.com',
            usuario='usuario',
            senha='senha',
            primeiro_nome='sim',
            segundo_nome='nao',
            endereco='Rua',
            cidade='Cidade ',
            idade=43
        )
        
        self.list_url = reverse('order-list', kwargs={'version': 'v1'}) 

        self.detail_url = reverse('order-detail', kwargs={'version': 'v1', 'pk': self.order.id})  

    def test_retrieve_order(self):
        response = self.client.get(self.detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_order(self):
        response = self.client.delete(self.detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        assert Order.objects.count() == 0  
