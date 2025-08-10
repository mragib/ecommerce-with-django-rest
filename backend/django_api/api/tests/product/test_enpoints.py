import pytest
import json

pytestmark = pytest.mark.django_db


class TestCategoryEndpoints:
    endpoint = "/product/category/"

    def test_get_all_category(self, category_factory, api_client):
        # Arrange
        category_factory.create_batch(5)

        # Act
        response = api_client().get(self.endpoint)

        # Assert
        assert response.status_code == 200

        assert len(json.loads(response.content)) == 5


class TestBrandEndpoints:
    endpoint = "/product/brand/"

    def test_get_all_brand(self, brand_factory, api_client):
        # Arrange
        brand_factory.create_batch(5)
        # Act
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200

        assert len(json.loads(response.content)) == 5


class TestProductEndpoints:
    endpoint = "/product/list/"

    def test_get_all_products(self, product_factory, api_client):
        # Arrange
        product_factory.create_batch(5)
        # Act
        response = api_client().get(self.endpoint)
        # Assert
        assert response.status_code == 200

        assert len(json.loads(response.content)) == 5
