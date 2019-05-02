from django import forms
from comercio.models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            'nome',
            'email',
            'endereco',
            'cartao',
            'pagamento'
        ]