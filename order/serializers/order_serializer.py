from rest_framework import serializers

from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id',                  
            'email',
            'usuario',
            'senha',
            'primeiro_nome',
            'segundo_nome',
            'endereco',
            'cidade',
            'idade'
        ]