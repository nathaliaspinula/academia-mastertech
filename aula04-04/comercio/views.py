from django.shortcuts import render
from comercio.forms import PedidoForm
# Create your views here.
def fazer_pedido(request):
    formulario = PedidoForm(request.POST or None)
    msg = ''
    if formulario.is_valid(): 
        formulario.save()
        formulario = PedidoForm()
        msg = 'Pedido realizado com sucesso'
    else: 
        msg = 'Error'
    
    content = {
        'form' : formulario,
        'msg' : msg
    }
    return render(request, 'index.html', context = content)
