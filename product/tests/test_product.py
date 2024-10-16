import pytest
from product.models import Product

@pytest.mark.django_db
def test_do_product():
    product = Product.objects.create(
        title="notebook",
        description="notebook do bom",
        price=True,  
        active=True
    )

    assert product.title == "notebook"
    assert product.description == "notebook do bom"
    assert product.price is True 
    assert product.active is True
    assert product.id is not None  
