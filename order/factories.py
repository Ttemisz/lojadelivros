import factory
from order.models import Order


class OrderFactory(factory.django.DjangoModelFactory):
    email = factory.Faker("pystr")
    usuario = factory.Faker("pystr")
    senha = factory.Faker("pystr")
    primeiro_nome = factory.Faker("pystr")
    segundo_nome = factory.Faker("pystr")
    endereco = factory.Faker("pystr")
    cidade = factory.Faker("pystr")
    idade = factory.Faker("random_int", min=0, max=99)

    class Meta:
        model = Order
