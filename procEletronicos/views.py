from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from .forms import ProcElet_Form, ValoresCalculos_Form
from .models import Procedimento_eletronico

def index_procedimentoElet(request):
    return render(request, 'procEletronicos/index.html')

#------------
class ProcElet_Create(CreateView):
    model = Procedimento_eletronico
    form_class = ProcElet_Form
    template_name = 'procEletronicos/procElet_create.html'
    success_url = '/'


class ProcElet_ListView(ListView):
    model = Procedimento_eletronico
    template_name = 'procEletronicos/procElet_list.html'
    context_object_name = 'procedimentos'

#------------



def valores_calculo(request):
    if request.method == 'POST':
        form = ValoresCalculos_Form(request.POST)
        if form.is_valid():
            # Recupere os valores dos campos de temperatura, umidade e pressão
            valor1 = request.POST.get('valor1')
            valor2 = request.POST.get('valor2')
            valor6 = request.POST.get('valor6')
            valor5 = request.POST.get('valor5')

            # Crie listas com os valores
            lista_valor = [valor1, valor2, valor6, valor5]


            # Atualize os campos 'temperatura', 'umidade' e 'pressao' do objeto Setor com as listas
            valores = form.save(commit=False)
            valores.valores = lista_valor
            valores.save()
            return redirect('/')  # Redirecionar após a criação bem-sucedida
    else:
        form = ValoresCalculos_Form()
    
    return render(request, 'procEletronicos/criar_calculos.html', {'form': form})