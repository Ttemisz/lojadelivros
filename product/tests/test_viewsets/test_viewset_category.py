from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from product.models.category import Category


class CategoryViewSetTestCase(APITestCase):

    def setUp(self):
        self.category = Category.objects.create(
            title="Categoria ", slug="categoria", description="Descricas", active=True
        )

        self.list_url = reverse("category-list", kwargs={"version": "v1"})

        self.detail_url = reverse(
            "category-detail", kwargs={"version": "v1", "pk": self.category.id}
        )

    def test_retrieve_category(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_category(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        assert Category.objects.count() == 0
