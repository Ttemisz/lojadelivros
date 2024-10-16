
import pytest

from order.models import Order

@pytest.mark.django_db
def test_create_user():
    
    usuario1 = Order.objects.create(
        email="test@example.com",
        usuario="test",
        senha="1233",
        primeiro_nome="jao",
        segundo_nome="pedro",
        endereco="igarassy",
        cidade="testedade",
        idade = 123
    )

    assert usuario1.email == "test@example.com"
    assert usuario1.usuario == "test"
    assert usuario1.senha == "1233"
    assert usuario1.primeiro_nome == "jao"
    assert usuario1.segundo_nome == "pedro"
    assert usuario1.endereco == "igarassy"
    assert usuario1.cidade == "testedade"
    assert usuario1.idade == 123
    assert usuario1.id is not None 