from django.db import models

class Order(models.Model):
    email = models.EmailField(default='email@exemplo.com')  # email 
    usuario = models.CharField(max_length=30, unique=True)  # suario
    senha = models.CharField(max_length=30)  # senha 
    primeiro_nome = models.CharField(max_length=20)  # primeiro nome
    segundo_nome = models.CharField(max_length=20)  # sobrenome
    endereco = models.TextField(max_length=100)  # endereço principal
    cidade = models.CharField(max_length=255, default='Cidade Padrão') #cidade
    idade = models.IntegerField(default=0) #idade

    def __str__(self):
        return self.email 

