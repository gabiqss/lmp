from django.shortcuts import render, redirect
from .models import Estoque, Setor
from .forms import EstoqueForm, SetorForm, AcreditacaoForm


def index(request):
    return render(request, 'comercial/index.html')


def area_acreditacao(request):
    if request.method == 'POST':
        form = AcreditacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 
    else:
        form = AcreditacaoForm()
    
    return render(request, 'comercial/area_acreditacao.html', {'form': form})


def criar_estoque(request):
    if request.method == 'POST':
        form = EstoqueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 
    else:
        form = EstoqueForm()
    
    return render(request, 'comercial/criar_estoque.html', {'form': form})




def criar_setor(request):
    if request.method == 'POST':
        form = SetorForm(request.POST)
        if form.is_valid():
            # Recupere os valores dos campos de temperatura, umidade e pressão
            temperatura_1 = request.POST.get('temperatura_1')
            temperatura_2 = request.POST.get('temperatura_2')
            temperatura_3 = request.POST.get('temperatura_3')

            umidade_1 = request.POST.get('umidade_1')
            umidade_2 = request.POST.get('umidade_2')
            umidade_3 = request.POST.get('umidade_3')

            pressao_1 = request.POST.get('pressao_1')
            pressao_2 = request.POST.get('pressao_2')
            pressao_3 = request.POST.get('pressao_3')

            # Crie listas com os valores de temperatura, umidade e pressão
            lista_temperatura = [temperatura_1, temperatura_2, temperatura_3]
            lista_umidade = [umidade_1, umidade_2, umidade_3]
            lista_pressao = [pressao_1, pressao_2, pressao_3]

            # Atualize os campos 'temperatura', 'umidade' e 'pressao' do objeto Setor com as listas
            setor = form.save(commit=False)
            setor.temperatura = lista_temperatura
            setor.umidade = lista_umidade
            setor.pressao = lista_pressao
            setor.save()
            return redirect('/')  # Redirecionar após a criação bem-sucedida
    else:
        form = SetorForm()
    
    return render(request, 'comercial/criar_setor.html', {'form': form})

