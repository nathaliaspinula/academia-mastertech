from django.db import models

# Create your models here.
class Produto (models.Model):
    nome = models.CharField(max_length = 100)
    preco = models.DecimalField(decimal_places = 2, max_digits = 100, default = 0)
    descricao = models.TextField(blank = True, null = True)
    em_estoque = models.BooleanField(default = True)

    def __str__(self):
        return self.nome

class Pedido (models.Model):
    pagamento_a_vista = 'av'
    pagamento_c_debito = 'cd'
    pagamento_c_credito = 'cc'
    pagamento_parcelado = 'pp'

    pagamento_opcoes = [
        (pagamento_a_vista, 'Pagamento à Vista'),
        (pagamento_c_debito, 'Cartão de Debito'),
        (pagamento_c_credito, 'Cartão de Crédito'),
        (pagamento_parcelado, 'Parcelado'),
    ]
    
    nome = models.CharField(max_length = 120)
    email = models.EmailField()
    endereco = models.CharField(max_length = 150)
    cartao = models.IntegerField()
    pagamento = models.CharField(max_length = 2, choices = pagamento_opcoes, default = pagamento_a_vista)

    def __str__(self):
        return self.nome