import pytest
from product.models import Category


@pytest.mark.django_db
def test_do_category():
    category = Category.objects.create(
        title="Livro de programacao",
        slug="livro-de-programacao",
        description="categoria dos livros de prog.",
        active=True,
    )

    assert category.title == "Livro de programacao"
    assert category.slug == "livro-de-programacao"
    assert category.description == "categoria dos livros de prog."
    assert category.active is True
    assert category.id is not None
