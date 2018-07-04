from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transacao
from .form import TransacaoForm
import datetime
# Create your views here.

def home(request):
    data={}
    data['transacoes'] = ['t1','t2','t3']

    data['now'] = datetime.datetime.now()
    #html = "<html><body>olá mundo, It is now %s.</body></html>" % now

    return render(request, 'contas/home.html', data)

# implementando o read no django
def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

#implementando o create nos formulários do django
def nova_transacao(request):
    form = TransacaoForm(request.POST or None)
    data = {}

    if form.is_valid():
        form.save()
        return redirect('url_listagem')
        #utilizar o redurect para evitar reanvio de formulario quando atualizar a pagina
    data ['form'] = form
    return render(request, 'contas/form.html', data)

# update no django
def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    data['form'] = form
    data['obj'] = transacao
    return render(request, 'contas/form.html', data)

# delete do django
def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')