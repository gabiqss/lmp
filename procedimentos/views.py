from django.shortcuts import render, redirect
from .models import Dados_procedimento, ArquivoPDF
from .forms import ProcedimentoForm, ArquivoPDFForm

def criar_procedimento(request):
    if request.method == 'POST':
        procedimento_form = ProcedimentoForm(request.POST)
        arquivo_form = ArquivoPDFForm(request.POST, request.FILES)
        if procedimento_form.is_valid() and arquivo_form.is_valid():
            procedimento = procedimento_form.save()  # Crie o procedimento primeiro

            # Crie instâncias de ArquivoPDF associadas ao procedimento
            for arquivo in request.FILES.getlist('arquivo'):
                ArquivoPDF.objects.create(arquivo=arquivo, procedimento=procedimento)

            return redirect('/')  # Redirecione para onde desejar após o procedimento ser criado
    else:
        procedimento_form = ProcedimentoForm()
        arquivo_form = ArquivoPDFForm()
    
    return render(request, 'procedimentos/criar_procedimentos.html', {'procedimento_form': procedimento_form, 'arquivo_form': arquivo_form})
