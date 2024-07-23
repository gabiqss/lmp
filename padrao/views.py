from django.shortcuts import render
from . models import *
from . forms import *
from django.views.generic import CreateView, ListView
from django.contrib import messages

#------------
def index(request):
    return render(request, 'padrao/index.html')

#------------
class GrandezaModelsView(CreateView):
    model = Grandeza
    form_class = GrandezaForm
    template_name = 'padrao/grandeza_create.html'
    success_url = '/'


class GrandezaListView(ListView):
    model = Grandeza
    template_name = 'padrao/grandeza_list.html'
    context_object_name = 'grandezas'

#------------
class UnidadeMedidaView(CreateView):
    model = Unidade_Medida
    form_class = Unidade_MedidaForm
    template_name = 'padrao/uni_medida_create.html'
    success_url = '/'


class UnidadeMedidaListView(ListView):
    model = Unidade_Medida
    template_name = 'padrao/uni_medida_list.html'
    context_object_name = 'unidadeMedida'

#------------

class ResolucaoView(CreateView):
    model = Resolucao
    form_class = ResolucaoForm
    template_name = 'padrao/resolucao_create.html'
    success_url = '/'

class ResolucaoListView(ListView):
    model = Resolucao
    template_name = 'padrao/resolucao_list.html'
    context_object_name = 'resolucoes'

#--------------

class Tipo_PadrãoView(CreateView):
    model = Tipo_Padrão
    form_class = Tipo_PadrãoForm
    template_name = 'padrao/tipo_padrao_create.html'
    success_url = '/'

class Tipo_PadrãoListView(ListView):
    model = Tipo_Padrão
    template_name = 'padrao/tipo_padrao_list.html'
    context_object_name = 'tipos_padrao'

#--------------

class FaixasFormView(CreateView):
    model = Faixas
    form_class = FaixasForm
    template_name = 'padrao/faixas_create.html'
    success_url = '/'

class FaixasFormListView(ListView):
    model = Faixas
    template_name = 'padrao/faixas_list.html'
    context_object_name = 'faixas'

#--------------

class Novo_PadrãoFormView(CreateView):
    model = Novo_Padrão
    form_class = Novo_PadrãoForm
    template_name = 'padrao/novo_padrao_create.html'
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request  # Passa o request para o formulário
        return kwargs
    def form_valid(self, form):
        tipo_instrumento = form.cleaned_data.get('tipo_instrumento')
        padrão_existente = Novo_Padrão.objects.filter(tipo_instrumento=tipo_instrumento).exists()

        if padrão_existente:
            messages.error(self.request, "Já existe um padrão com este tipo de instrumento.")
            return self.form_invalid(form)

        return super().form_valid(form)
    
class Novo_PadrãoFormListView(ListView):
    model = Novo_Padrão
    template_name = 'padrao/novo_padrao_list.html'
    context_object_name = 'novosPadrao'


#--------------

class Criterio_AceitacaoView(CreateView):
    model = Criterio_Aceitacao
    form_class = Criterio_AceitacaoForm
    template_name = 'padrao/criterio_aceitacao_create.html'
    success_url = '/'

class Criterio_AceitacaoListView(ListView):
    model = Criterio_Aceitacao
    template_name = 'padrao/criterio_aceitacao_list.html'
    context_object_name = 'criterios_aceitacao'


#--------------



