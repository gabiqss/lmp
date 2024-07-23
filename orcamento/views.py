from django.shortcuts import redirect, render
from instruments.models import InstrumentsInstruments
from main.models import Contacts_Customers, Customers_main
from accounts.models import CustomUser
from accounts.forms import CustomUserCreationForm
from main.forms import *
from itertools import chain
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from procEletronicos.models import Procedimento_eletronico
from orcamento.forms import *
from orcamento.models import *
from orcamento.consts import StatusOrcamentos
from instruments.models import InstrumentsInstruments, InstrumentTypes
from django.contrib import messages
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.pdfgen import canvas
import locale
import pandas as pd
from django.conf import settings
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.db.models import Q, Max
from datetime import datetime
from django.contrib.auth.decorators import login_required

def servico_calibracao_create(request):
    if request.method == 'POST':
        form_servico_calibracao = ServicoCalibracaoForm(request.POST)
        if form_servico_calibracao.is_valid():
            form_servico_calibracao.save()
    else:
        form_servico_calibracao = ServicoCalibracaoForm()
        print(form_servico_calibracao.errors)
    return render(request, 'orcamento_criar.html', {'form_servico_calibracao': form_servico_calibracao})

def delete_servico_calibracao(request, id):
    servico_calibracao = get_object_or_404(ServicoCalibracao, id=id)
    servico_calibracao.delete()
    return redirect('orcamento_create')

def servico_ensaio_create(request):
    if request.method == 'POST':
        form_servico_ensaio = ServicoEnsaioForm(request.POST)
        if form_servico_ensaio.is_valid():
            form_servico_ensaio.save()
    else:
        form_servico_ensaio = ServicoEnsaioForm()
    return render(request, 'orcamento_criar.html', {'form_servico_ensaio': form_servico_ensaio})

def delete_servico_ensaio(request, id):
    servico_ensaio = get_object_or_404(ServicoEnsaio, id=id)
    servico_ensaio.delete()
    return redirect('orcamento_create')

def servico_manutencao_create(request):
    if request.method == 'POST':
        form_servico_manutencao = ServicoManutencaoForm(request.POST)
        if form_servico_manutencao.is_valid():
            form_servico_manutencao.save()
    else:
        form_servico_manutencao = ServicoManutencaoForm()
    return render(request, 'orcamento_criar.html', {'form_servico_manutencao': form_servico_manutencao})

def delete_servico_manutencao(request, id):
    servico_manutencao = get_object_or_404(ServicoManutencao, id=id)
    servico_manutencao.delete()
    return redirect('orcamento_create')

def servico_qt_create(request):
    if request.method == 'POST':
        form_servico_qt = ServicoQTForm(request.POST)
        if form_servico_qt.is_valid():
            form_servico_qt.save()
    else:
        form_servico_qt = ServicoQTForm()
    return render(request, 'orcamento_criar.html', {'form_servico_qt': form_servico_qt})

def delete_servico_qt(request, id):
    servico_qt = get_object_or_404(ServicoQT, id=id)
    servico_qt.delete()
    return redirect('orcamento_create')

def tipo_orcamento_create(request):
    if request.method == 'POST':
        form_tipo_orcamento = OrcamentoTipoForm(request.POST)
        if form_tipo_orcamento.is_valid():
            form_tipo_orcamento.save()
    else:
        form_tipo_orcamento = OrcamentoTipoForm()
    return render(request, 'orcamento_criar.html', {'form_tipo_orcamento': form_tipo_orcamento})

def delete_tipo_orcamento(request, id):
    tipo_orcamento = get_object_or_404(TipoOrcamento, id=id)
    tipo_orcamento.delete()
    return redirect('orcamento_create')

def solicitacao_create(request):
    if request.method == 'POST':
        form_solicitacao = SolicitacaoForm(request.POST)
        if form_solicitacao.is_valid():
            form_solicitacao.save()
    else:
        form_solicitacao = SolicitacaoForm()
    return render(request, 'orcamento_criar.html', {'form_solicitacao': form_solicitacao})

def delete_solicitacao(request, id):
    solicitacao = get_object_or_404(Solicitacao, id=id)
    solicitacao.delete()
    return redirect('/orcamento/orcamento/create/')

def pagamento_condicao_create(request):
    if request.method == 'POST':
        form_pagamento_condicao = PagamentoCondicaoForm(request.POST)
        if form_pagamento_condicao.is_valid():
            form_pagamento_condicao.save()
    else:
        form_pagamento_condicao = PagamentoCondicaoForm()
    return render(request, 'orcamento_criar.html', {'form_pagamento_condicao': form_pagamento_condicao})

def delete_pagamento_condicao(request, id):
    pagamento_condicao = get_object_or_404(PagamentoCondicao, id=id)
    pagamento_condicao.delete()
    return redirect('/orcamento/orcamento/create/')

def responsavel_create(request):
    if request.method == 'POST':
        form_responsavel = CustomUserCreationForm(request.POST)
        if form_responsavel.is_valid():
            form_responsavel.save()
    else:
        form_responsavel = CustomUserCreationForm()
    return render(request, 'orcamento_criar.html', {'form_responsavel': form_responsavel})

def delete_responsavel(request, id):
    responsavel = get_object_or_404(CustomUser, id=id)
    responsavel.delete()
    return redirect('/orcamento/orcamento/create/')

def pagamento_forma_create(request):
    if request.method == 'POST':
        form_pagamento_forma = PagamentoFormaForm(request.POST)
        if form_pagamento_forma.is_valid():
            form_pagamento_forma.save()
    else:
        form_pagamento_forma = PagamentoFormaForm()
    return render(request, 'orcamento_criar.html', {'form_pagamento_forma': form_pagamento_forma})

def delete_pagamento_forma(request, id):
    pagamento_forma = get_object_or_404(PagamentoForma, id=id)
    pagamento_forma.delete()
    return redirect('/orcamento/orcamento/create/')

def contato_create(request):
    if request.method == 'POST':
        form_contato = Contatos_Clientes_select(request.POST)
        if form_contato.is_valid():
            form_contato.save()
    else:
        form_contato = Contatos_Clientes_select()
    return render(request, 'orcamento_criar.html', {'form_contato': form_contato})

def delete_contato(request, id):
    contato = get_object_or_404(Contacts_Customers, id=id)
    contato.delete()
    return redirect('/orcamento/orcamento/create/')

def cliente_cnpj_create(request):
    if request.method == 'POST':
        form = Cadatrar_Clientes(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomUserCreationForm()
    return render(request, 'orcamento_criar.html', {'form_cliente_cpnj': form})

def cliente_cpf_create(request):
    if request.method == 'POST':
        form = Cadatrar_Clientes_CPF(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomUserCreationForm()
    return render(request, 'orcamento_criar.html', {'form_cliente_cpf': form})

def cliente_delete(request, id):
    cliente = get_object_or_404(Customers_main, id=id)
    cliente.delete()
    return redirect('/orcamento/orcamento/create/')

def view_orcamento(request):
    revisoes = OrcamentoAtividade.objects.all()
    orcamentos = Orcamento.objects.all()
    alteracoes = OrcamentoAtividade.objects.filter(orcamento__in=orcamentos)
    barra_pesquisa = request.GET.get("search")
    if barra_pesquisa:
        try:
            data_pesquisa = datetime.strptime(barra_pesquisa, '%d/%m/%Y').date()
        except ValueError:
            # Em caso de erro na conversão, trate como uma string normal
            data_pesquisa = barra_pesquisa
        orcamentos = orcamentos.filter(
            Q(solicitante__cnpj__icontains=barra_pesquisa) |
            Q(solicitante__name__icontains=barra_pesquisa) |
            Q(contato__name__icontains=barra_pesquisa) |
            Q(status__icontains=barra_pesquisa) |
            Q(data_cadastro__icontains=data_pesquisa)
        )
    opened_os_count = orcamentos.filter(status=StatusOrcamentos.OPEN).count()
    await_payment_count = orcamentos.filter(
        status=StatusOrcamentos.AWAIT_PAYMENT
    ).count()
    made_payment_count = orcamentos.filter(status=StatusOrcamentos.MADE_PAYMENT).count()
    canceled_count = orcamentos.filter(status=StatusOrcamentos.CANCELED).count()
    return render(
        request,
        "view_orcamento.html",
        {
            "revisoes": revisoes,
            "orcamentos": orcamentos,
            "opened_os_count": opened_os_count,
            "await_payment_count": await_payment_count,
            "made_payment_count": made_payment_count,
            "canceled_count": canceled_count,
            "barra_pesquisa": barra_pesquisa,
            "alteracoes": alteracoes
        },
    )


def view_equipamentos(request, id_orcamento):
    equipamentos = Equipamento.objects.filter(orcamento__id=id_orcamento)
    return render(
        request,
        "equipamentos.html",
        {"equipamentos": equipamentos, "id_orcamento": id_orcamento},
    )


def create_equipamento(request, id_orcamento):
    cliente = Orcamento.objects.get(pk=id_orcamento)

    form = EquipamentoForm(
        initial={"orcamento": id_orcamento, "solicitante": cliente.solicitante}
    )

    if request.method == "POST":
        request.POST._mutable = True
        request.POST["orcamento"] = id_orcamento
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            equipamento = form.save(commit=False)
            equipamento.save()
            return redirect(f"/orcamento/{id_orcamento}/equipamentos/")
        else:
            print(form.errors)
    return render(request, "new_equipamento.html", {"form": form})


def create_dados_de_pagamento_orcamento(request, id_orcamento):
    orcamento = get_object_or_404(Orcamento, id=id_orcamento)
    if Equipamento.objects.filter(orcamento=orcamento).count() == 0:
        messages.warning(request, "Não é possível criar um orçamento sem equipamentos!")
        return redirect(f"/orcamento/{id_orcamento}/equipamentos/")
    form = DadosDePagamentoForm(
        initial={
            "orcamento": id_orcamento,
        }
    )
    if request.method == "POST":
        request.POST._mutable = True
        request.POST["orcamento"] = id_orcamento
        form = DadosDePagamentoForm(request.POST)
        if form.is_valid():
            equipamento = form.save(commit=False)
            equipamento.save()
            messages.success(request, "Orçamento cadastrado com sucesso!")
            return redirect(f"/orcamento/orcamentos")
    return render(request, "pagamento.html", {"form_payments": form})


def orcamento_detail_view(request, id_orcamento):
    orcamento = Orcamento.objects.get(id=id_orcamento)
    servicos = ServicosOrcamento.objects.filter(orcamento=orcamento)
    anexos = AnexosOrcamento.objects.filter(orcamento=orcamento)
    return render(
        request,
        "detail_orcamento.html",
        {"orcamento": orcamento, "servicos": servicos, "anexos": anexos},
    )


def create_solicitante(request):
    form_cliente = Cadatrar_Clientes()
    form_contato = Contatos_Clientes()
    customers = Customers_main.objects.values("id", "name").distinct().order_by("name")
    selected_customer = None
    selected_contacts = None
    customer_id = request.GET.get("id_customer")

    if customer_id is not None and int(customer_id) != 0:
        selected_customer = Customers_main.objects.get(id=customer_id)
        selected_contacts = Contacts_Customers.objects.filter(id_customer=customer_id)
        form = OrcamentoForm(
            initial={
                "solicitante": selected_customer.name,
            }
        )
        if request.method == "POST":
            form = OrcamentoForm(
                request.POST,
                initial={
                    "solicitante": selected_customer.name,
                },
            )
            if form.is_valid():
                orcamento = form.save(commit=False)
                orcamento.save()
                return redirect("orcamento_create")

    else:
        form = OrcamentoForm()
    return render(
        request,
        "solicitante.html",
        {
            "form": form,
            "form_contato": form_contato,
            "form_cliente": form_cliente,
            "customers": customers,
            "selected_customer": selected_customer,
            "selected_contacts": selected_contacts,
        },
    )
import json
from django.http import JsonResponse

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .forms import OrcamentoForm, AnexosOrcamentoForm, ServicosOrcamentoForm
from .models import Orcamento, AnexosOrcamento, ServicosOrcamento
import json

from django.views.generic.edit import UpdateView 

from django.views.generic import UpdateView, CreateView
from .models import Orcamento
from .forms import OrcamentoForm
from django.urls import reverse
from django.urls import reverse_lazy



class OrcamentoUpdateView(UpdateView):
    model = Orcamento
    template_name = "orcamento_criar.html"
    fields = "__all__"
    success_url = reverse_lazy('view-orcamento')

    def form_valid(self, form):
        tipo_salvamento = self.request.POST.get('tipo_salvamento')
        print(tipo_salvamento)
        if tipo_salvamento == 'novo':
            
            # Obtenha o objeto 
            orcamento = self.get_object()
            orcamento_raiz = orcamento.orcamento_raiz
            solicitante = form.cleaned_data.get('solicitante')
            responsavel = form.cleaned_data.get('responsavel')
            contato = form.cleaned_data.get('contato')
            data_cadastro = form.cleaned_data.get('data_cadastro')
            validade_proposta = form.cleaned_data.get('validade_proposta')
            observacoes = form.cleaned_data.get('observacoes')
            forma_pagamento = form.cleaned_data.get('forma_pagamento')
            local = form.cleaned_data.get('local')
            contrato = form.cleaned_data.get('contrato')
            tipo_de_desconto = form.cleaned_data.get('tipo_de_desconto')
            desconto = form.cleaned_data.get('desconto')
            acrescimo = form.cleaned_data.get('acrescimo')
            condicao_pagamento = form.cleaned_data.get('condicao_pagamento')
            tipo_orcamento = form.cleaned_data.get('tipo_orcamento')
            forma_solicitacao = form.cleaned_data.get('forma_solicitacao')

            # Parâmetro encontrado, faça algo com ele
            orcamento_revisado = Orcamento.objects.create(
                orcamento_raiz=orcamento_raiz,
                solicitante=solicitante,
                responsavel=responsavel,
                contato=contato,
                data_cadastro=data_cadastro,
                validade_proposta=validade_proposta,
                observacoes=observacoes,
                forma_pagamento=forma_pagamento,
                local=local,
                contrato=contrato,
                tipo_de_desconto=tipo_de_desconto,
                desconto=desconto,
                acrescimo=acrescimo,
                condicao_pagamento=condicao_pagamento,
                tipo_orcamento=tipo_orcamento,
                forma_solicitacao=forma_solicitacao
            )
            return HttpResponseRedirect(self.get_success_url())
        
        else:
            orcamento = form.save(commit=False)
            orcamento.save()

            valores_selecionados = self.request.POST.getlist('valoresSelecionados')
            for item in valores_selecionados:
                if len(item) == 2:
                    # Delete objects of ServicosOrcamento associated with the budget
                    ServicosOrcamento.objects.filter(orcamento=orcamento).delete()
                else:
                    lista_dicionarios = json.loads(item)
                    for dicionario in lista_dicionarios:
                        ServicosOrcamento.objects.create(
                            orcamento=orcamento,
                            codigo=dicionario.get('codigo', 'N/A'),
                            especificacao=dicionario.get('especificacao', 'N/A'),
                            area_acreditacao=dicionario.get('area_acreditacao', 'N/A'),
                            tipo_calibracao=dicionario.get('tipo_calibracao', 'N/A'),
                            tipo_item=dicionario.get('tipo_item', 'N/A'),
                            local=dicionario.get('local', 'N/A'),
                            descricao=dicionario.get('descricao', 'N/A'),
                            pontos=dicionario.get('pontos', 'N/A'),
                            pontos_valor_adicional=dicionario.get('pontos_valor_adicional', 'N/A'),
                            valor=dicionario.get('valor', 'N/A'),
                            tipo_servico=dicionario.get('tipo_servico', 'N/A'),
                        )

            # Adicionando anexos do orcamento
            anexo_form = AnexosOrcamentoForm(self.request.POST, self.request.FILES, initial={'orcamento': orcamento})
            if anexo_form.is_valid():
                for file in self.request.FILES.getlist('anexo'):
                    AnexosOrcamento.objects.create(
                        orcamento=orcamento,
                        anexo=file
                    )

        return super().form_valid(form)

    

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['status'].initial = self.object.status
        return form

    def get_absolute_url(self):
        return reverse('view-orcamento')
    
    def get_context_data(self, **kwargs):
        orcamento_id = self.object.id
        servicos = ServicosOrcamento.objects.filter(orcamento=orcamento_id)
        lista_codigos = []
        
        context = super().get_context_data(**kwargs)
        context['orcamento_id'] = orcamento_id
        context['clientes'] = Customers_main.objects.all()
        context['contatos'] = Contacts_Customers.objects.all()
        context['tipos_orcamento'] = TipoOrcamento.objects.all()
        context['solicitacao'] = Solicitacao.objects.all()
        context['forma'] = PagamentoForma.objects.all()
        context['condicoes'] = PagamentoCondicao.objects.all()
        context['responsaveis'] = CustomUser.objects.all()
        context['servico_calibracao'] = ServicoCalibracao.objects.all()
        context['servico_ensaio'] = ServicoEnsaio.objects.all()
        context['servico_manutencao'] = ServicoManutencao.objects.all()
        context['servico_qt'] = ServicoQT.objects.all()
        context['form_cliente'] = Cadatrar_Clientes()
        context['form_cliente_cpf'] = Cadatrar_Clientes_CPF()
        context['form_contato'] = Contatos_Clientes_select()
        context['form_tipo_orcamento'] = OrcamentoTipoForm()
        context['form_solicitacao'] = SolicitacaoForm()
        context['form_pagamento_forma'] = PagamentoFormaForm()
        context['form_pagamento_condicao'] = PagamentoCondicaoForm()
        context['form_responsaveis'] = CustomUserCreationForm()
        context['form_servico_calibracao'] = ServicoCalibracaoForm()
        context['form_servico_ensaio'] = ServicoEnsaioForm()
        context['form_servico_manutencao'] = ServicoManutencaoForm()
        context['form_servico_qt'] = ServicoQTForm()
        context['anexo_form'] = AnexosOrcamentoForm()
        context['arquivo'] = (AnexosOrcamento.objects.filter(orcamento=orcamento_id))
        context['form_servico_orcamento'] = ServicosOrcamentoForm()
        context['dados'] = []
        context['contato_atual'] = self.object.contato.id if self.object.contato else None
        context['condicao_pagamento'] = self.object.condicao_pagamento if self.object.condicao_pagamento else None
        context['forma_pagamento'] = self.object.forma_pagamento if self.object.forma_pagamento else None
        context['forma_solicitacao'] = self.object.forma_solicitacao if self.object.forma_solicitacao else None
        context['tipo_orcamento'] = self.object.tipo_orcamento if self.object.tipo_orcamento else None
        context['listaservicos'] = servicos
        desconto = Orcamento.objects.filter(id=orcamento_id)
        context['desconto'] = (desconto[0].desconto)
        acrescimo = Orcamento.objects.filter(id=orcamento_id)
        context['acrescimo'] = (acrescimo[0].acrescimo)
        tipo_de_desconto = Orcamento.objects.filter(id=orcamento_id)
        context['tipo_de_desconto'] = tipo_de_desconto[0].tipo_de_desconto
        status = Orcamento.objects.filter(id=orcamento_id)
        status_choices = {"Aberto": "Aberto",
            "Fechado": "Fechado",
            "Revisado": "Revisado",
            "Cancelado": "Cancelado"}
        contrato_choices = {"Sim": "Sim",
            "Não": "Não"}
        context['proximo_id'] = status[0].orcamento_raiz
        context['contrato'] = status[0].contrato
        context['contrato_choices'] = contrato_choices.values()   
        context['status'] = status[0].status
        context['status_choices'] = status_choices.values()
        orcamento = Orcamento.objects.filter(id=orcamento_id)
        context['data_cadastro'] = datetime.strftime(orcamento[0].data_cadastro, "%Y-%m-%d")
        if orcamento[0].validade_proposta:
            context['validade_proposta'] = datetime.strftime(orcamento[0].validade_proposta, "%Y-%m-%d")
        else:
            context['validade_proposta'] = None
        local_choices = {"LEMPE": "LEMPE",
            "In Loco": "In Loco"}
        context['local'] = status[0].local
        context['local_choices'] = local_choices.values() 
        for servico in context['listaservicos']:
            lista_codigos.append(servico.codigo)
        context['servicos_json'] = json.dumps(lista_codigos)
        return context

def orcamento_revisao_view(request, orcamento_id):
    orcamento = get_object_or_404(Orcamento, pk=orcamento_id)
    form = OrcamentoForm(request.POST or None, instance=orcamento)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Orcamento atualizado com sucesso!")
        return redirect("view-orcamento")
    else:
        print(form.errors)
    return render(request, 'orcamento_criar.html')

def orcamento_create_or_update_view(request, orcamento_id=None):
    if orcamento_id:
        orcamento = get_object_or_404(Orcamento, pk=orcamento_id)
        form = OrcamentoForm(request.POST or None, instance=orcamento)
    else:
        orcamento = None
        form = OrcamentoForm(request.POST or None)
    status_choices = {"Aberto": "Aberto",
            "Fechado": "Fechado",
            "Revisado": "Revisado",
            "Cancelado": "Cancelado"}
    contrato_choices = {"Sim": "Sim",
            "Não": "Não"}
    local_choices = {"LEMPE": "LEMPE",
            "In Loco": "In Loco"}
    clientes = Customers_main.objects.all()
    contatos = Contacts_Customers.objects.all()
    tipos_orcamento = TipoOrcamento.objects.all()
    solicitacao = Solicitacao.objects.all()
    forma = PagamentoForma.objects.all()
    condicao = PagamentoCondicao.objects.all()
    responsaveis = CustomUser.objects.all()
    servico_calibracao = ServicoCalibracao.objects.all()
    servico_ensaio = ServicoEnsaio.objects.all()
    servico_manutencao = ServicoManutencao.objects.all()
    servico_qt = ServicoQT.objects.all()
    form_cliente = Cadatrar_Clientes()
    form_cliente_cpf = Cadatrar_Clientes_CPF()
    form_contato = Contatos_Clientes_select()
    form_tipo_orcamento = OrcamentoTipoForm()
    form_solicitacao = SolicitacaoForm()
    form_pagamento_forma = PagamentoFormaForm()
    form_pagamento_condicao = PagamentoCondicaoForm()
    form_responsaveis = CustomUserCreationForm()
    form_servico_calibracao = ServicoCalibracaoForm()
    form_servico_ensaio = ServicoEnsaioForm()
    form_servico_manutencao = ServicoManutencaoForm()
    form_servico_qt = ServicoQTForm()
    anexo_form = AnexosOrcamentoForm()
    form_servico_orcamento = ServicosOrcamentoForm()
    barra_pesquisa = request.GET.get("search")
    dados = []
    ultimo_orcamento = Orcamento.objects.order_by('-id').first()

    print(ultimo_orcamento) 

    # Obter o ID do último objeto, se existir
    ultimo_id = ultimo_orcamento.id if ultimo_orcamento else 0

    print("ultimo:", ultimo_id)

    if orcamento == None:
        proximo_id = ultimo_id + 1
    else:
        proximo_id = orcamento.orcamento_raiz
    print("ID:", proximo_id)
    if request.method == 'POST' and form.is_valid():
        orcamento = form.save(commit=False)
        orcamento.orcamento_raiz = proximo_id
        orcamento.save()  # Salvar no banco de dados
        valores_selecionados = request.POST.getlist('valoresSelecionados')
        print("valores : ", valores_selecionados)
        for item in valores_selecionados:
            lista_dicionarios = json.loads(item)
            for dicionario in lista_dicionarios:
                ServicosOrcamento.objects.create(
                    orcamento=orcamento,
                    codigo=dicionario.get('codigo', 'N/A'),
                    especificacao=dicionario.get('especificacao', 'N/A'),
                    area_acreditacao=dicionario.get('area_acreditacao', 'N/A'),
                    tipo_calibracao=dicionario.get('tipo_calibracao', 'N/A'),
                    tipo_item=dicionario.get('tipo_item', 'N/A'),
                    local=dicionario.get('local', 'N/A'),
                    descricao=dicionario.get('descricao', 'N/A'),
                    pontos=dicionario.get('pontos', 'N/A'),
                    pontos_valor_adicional=dicionario.get('pontos_valor_adicional', 'N/A'),
                    valor=dicionario.get('valor', 'N/A'),
                    tipo_servico=dicionario.get('tipo_servico', 'N/A'),
                )

        anexo_form = AnexosOrcamentoForm(request.POST, request.FILES, initial={'orcamento': orcamento})
        if anexo_form.is_valid():
            for file in request.FILES.getlist('anexo'):
                AnexosOrcamento.objects.create(
                    orcamento=orcamento,
                    anexo=file
                )
        else:
            pass

        messages.success(request, "Orçamento criado/atualizado com sucesso!")
        return redirect("view-orcamento")

    else:
        print(form.errors, anexo_form.errors, form_servico_orcamento.errors)
        for field, errors in form.errors.items():
            print(f"Campo: {field}, valor: {form.data.get(field)}")

    return render(request, 'orcamento_criar.html', {
        'form': form,
        'form_cliente_cpf': form_cliente_cpf,
        'form_contato': form_contato,
        'form_cliente': form_cliente,
        'form_tipo_orcamento': form_tipo_orcamento,
        'clientes': clientes,
        'contatos': contatos,
        'tipos_orcamento': tipos_orcamento,
        'solicitacao': solicitacao,
        'forma': forma,
        'condicoes': condicao,
        'form_solicitacao': form_solicitacao,
        'form_pagamento_forma': form_pagamento_forma,
        'form_pagamento_condicao': form_pagamento_condicao,
        'form_responsaveis': form_responsaveis,
        'responsaveis': responsaveis,
        'form_anexo': anexo_form,
        'servico_calibracao': servico_calibracao,
        'servico_ensaio': servico_ensaio,
        'servico_manutencao': servico_manutencao,
        'servico_qt': servico_qt,
        'form_servico_calibracao': form_servico_calibracao,
        'form_servico_ensaio': form_servico_ensaio,
        'form_servico_manutencao': form_servico_manutencao,
        'form_servico_qt': form_servico_qt,
        'barra_pesquisa': barra_pesquisa,
        'dados': dados,
        'status_choices': status_choices.values(),
        'contrato_choices': contrato_choices.values(),
        'local_choices': local_choices.values(),
        'proximo_id': proximo_id
    })


@login_required
def orcamento_alterar(request, id_orcamento):
    orcamento = get_object_or_404(Orcamento, id=id_orcamento)
    usuario = request.user
    
    if request.method == 'POST':
        orcamento_form = OrcamentoForm(request.POST, instance=orcamento)
        atividade_form = OrcamentoAtividadeForm(request.POST)
        anexos_form = AnexosOrcamentoAtividadeForm(request.POST, request.FILES)
        servicos_form = ServicosOrcamentoAtividadeForm(request.POST)
        
        if orcamento_form.is_valid() and atividade_form.is_valid() and anexos_form.is_valid() and servicos_form.is_valid():
            orcamento = orcamento_form.save()
            atividade = atividade_form.save(commit=False)
            atividade.responsavel_atividade = usuario
            atividade.orcamento = orcamento
            atividade.save()
            anexos_form.instance.atividade = atividade
            anexos_form.save()
            servicos_form.instance.atividade = atividade
            servicos_form.save()
            return redirect('view-orcamento')
    else:
        orcamento_form = OrcamentoForm(instance=orcamento)
        atividade_form = OrcamentoAtividadeForm(instance=orcamento, initial={'responsavel_atividade': usuario})
        anexos_form = AnexosOrcamentoAtividadeForm(instance=orcamento)
        servicos_form = ServicosOrcamentoAtividadeForm()

        # Preencher manualmente os campos Select2
        atividade_form.fields['solicitante'].queryset = Customers_main.objects.filter(pk=orcamento.solicitante.pk)
        atividade_form.fields['contato'].queryset = Contacts_Customers.objects.filter(pk=orcamento.contato.pk)

        # Preencher manualmente os campos de data
        atividade_form.initial['data_cadastro'] = datetime.strftime(orcamento.data_cadastro, "%Y-%m-%d")
        atividade_form.initial['data_atualizacao'] = orcamento.data_atualizacao
        atividade_form.initial['validade_proposta'] = datetime.strftime(orcamento.validade_proposta, "%Y-%m-%d")
        atividade_form.initial['forma_pagamento'] = orcamento.forma_pagamento
        atividade_form.initial['condicao_pagamento'] = orcamento.condicao_pagamento
        atividade_form.initial['tipo_orcamento'] = orcamento.tipo_orcamento
        atividade_form.initial['forma_solicitacao'] = orcamento.forma_solicitacao
    
    return render(request, 'orcamento_alterar.html', {
        'orcamento': orcamento,
        'orcamento_form': orcamento_form,
        'atividade_form': atividade_form,
        'anexos_form': anexos_form,
        'servicos_form': servicos_form,
    })

def orcamento_detail_view(request, id_orcamento):
    orcamento = Orcamento.objects.get(id=id_orcamento)
    servicos = ServicosOrcamento.objects.filter(orcamento=orcamento)

    desconto = float(orcamento.desconto) if orcamento and orcamento.desconto else 0
    acrescimo = float(orcamento.acrescimo) if orcamento and orcamento.acrescimo else 0
    total = 0  # Definindo um valor padrão para total

    for servico_obj in servicos:
        total += float(servico_obj.valor)

    if orcamento.tipo_de_desconto == 'porcentagem':
        valor_desconto = (desconto / 100) * total
        total -= valor_desconto
    elif orcamento.tipo_de_desconto == 'valor_real':
        total -= desconto

    total += acrescimo

    total = str(total)
    
    anexos = AnexosOrcamento.objects.filter(orcamento=orcamento)
    return render(
        request,
        "orcamento.html",
        {"orcamento": orcamento, "servicos": servicos, "anexos": anexos, "total": total},
    )

def orcamento_edit_view(request, id_orcamento):
    orcamento = get_object_or_404(Orcamento, id=id_orcamento)
    form = OrcamentoForm(request.POST or None, instance=orcamento)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            # Redirecione ou retorne uma resposta adequada após o salvamento
            return redirect('/orcamento/orcamentos')
        else:
            print("Formulário inválido. Erros:", 'form.errors', form.errors)

    return render(request, 'edit_orcamento.html', {'form': form, 'orcamento': orcamento})

def orcamento_delete_view(request, id_orcamento):
    orcamento = get_object_or_404(Orcamento, id=id_orcamento)
    orcamento.delete()
    return redirect('/orcamento/orcamentos')

def orcamento_pdf_view(request, id_orcamento):
    # Configurar a localidade para tratar números com vírgulas
    
    orcamento = Orcamento.objects.get(id=id_orcamento)
    servico= ServicosOrcamento.objects.filter(orcamento=orcamento)
    # Verifica se equipamentos é diferente de None e se equipamentos.peca existe
    #instrument = equipamentos.peca if equipamentos and hasattr(equipamentos, 'peca') else 'N/A'

    # Verifica se instrument é diferente de 'N/A' e se instrument.id_instrument_type existe
    #instrument_type = (
    #    instrument.id_instrument_type if instrument and hasattr(instrument, 'id_instrument_type') else 'N/A'
    #)

    #print(instrument_type)

    # Verifica se instrument_type é diferente de 'N/A' antes de usar na query
    #if instrument_type != 'N/A':
    #    procedimento = Procedimento_eletronico.objects.filter(tipo_instrumento=instrument_type).first()
    #else:
    #    procedimento = None  # Ou defina procedimento como desejado se instrument_type for 'N/A'
    #print(procedimento)
    contato = orcamento.contato
    customer = contato.id_customer
    ano_atual = datetime.now().year

    # Restaurar a localidade padrão

    # Criar o caminho completo do arquivo PDF
    pdf_file_path = f"{settings.MEDIA_ROOT}/exemplo.pdf"
    pdf = canvas.Canvas(pdf_file_path, pagesize=letter)
    

    # Function for the first part of the certificate
    def primeira_parte_pdf(pdf):
        pdf.drawInlineImage(
            r'static/img/Imagem - de cima.jpeg',
            50, 700,
            preserveAspectRatio=True
        )
        if Orcamento.objects.filter(orcamento_raiz=orcamento.orcamento_raiz).count() > 1:
            # Obtém o número total de revisões para este orçamento raiz
            revisoes_totais = Orcamento.objects.filter(orcamento_raiz=orcamento.orcamento_raiz).count() - 1
            # Obtém o número de revisão específico para este orçamento
            revisao_atual = Orcamento.objects.filter(orcamento_raiz=orcamento.orcamento_raiz).filter(pk__lte=orcamento.pk).count() - 1
            # Adiciona a contagem de revisão específica se houver mais de uma revisão
            contagem = 'R{}'.format(revisao_atual) if revisoes_totais > 0 else ''
            # Monta o ID do orçamento com a contagem de revisão
            id_orc = orcamento.orcamento_raiz
        else:
            contagem = ''
            id_orc = orcamento.orcamento_raiz
        # Verifica se a contagem não é 'R0' para deixar vazio caso seja 'R0'
        if contagem == 'R0':
            contagem = ''
        pdf.setFontSize(15)
        pdf.setFillColor(colors.black)
        pdf.drawCentredString(480,734,'Orçamento nº: {}/{} {}'.format(id_orc, ano_atual, contagem))
        pdf.setFontSize(9)

        # Colocando os textos em negrito: 

        pdf.setFont("Helvetica-Bold",9)

        # Colocando titulos referentes aos dados: 

        pdf.setFontSize(9)
        pdf.drawCentredString(115,685,'1 - DADOS DO CLIENTE')


        pdf.drawCentredString(85,670,'De:')
        pdf.drawCentredString(150,670,str(orcamento.responsavel))


        pdf.drawCentredString(90,652,'Para:')
        pdf.drawCentredString(150,652,str(contato.name))

        pdf.drawCentredString(95,634,'Empresa:')
        pdf.drawCentredString(240,634,str(customer.name))

        pdf.drawCentredString(90,616,'E-mail:')
        pdf.drawCentredString(165,616,str(contato.email))

        pdf.drawCentredString(430,670,'Validade do Orçamento:')
        pdf.drawCentredString(550,670,'30 dias após a emissão')

        pdf.drawCentredString(425,652,'Telefone/Fax:')
        pdf.drawCentredString(500,652, str(contato.commercial_phone) or str(contato.cellular) or str(customer.fax))

        pdf.drawCentredString(435,634,'Setor/Cargo:')
        pdf.drawCentredString(495,634,str(contato.sector))

        data_emissao = orcamento.data_cadastro.strftime('%d/%m/%Y')
        pdf.drawCentredString(440,616,'Data de Emissão:')
        pdf.drawCentredString(515,616,str(data_emissao))

        
        # 2 - CONDIÇÕES GERAIS: 

        
        pdf.drawCentredString(115,605,'2 - CONDIÇÕES GERAIS')

        tex = Paragraph("1. Em caso de troca de equipamentos de venda, tem o prazo de 7 dias corridos desde que o equipamento esteja com a embalagem e manual, após esse prazo só poderá ser realizado diretamente com o fabricante.") # instanciando o paragrafo depois de importar a biblioteca
        tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,75,577)
        tex = Paragraph("2. Não estão inclusas as despesas de viagem, hospedagem, alimentação, translado,excesso de bagagem e envio de equipamentos.")
        tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,75,552)
        tex = Paragraph("3. Para os serviços executados no laboratório do cliente, o mesmo deve fornecer um ambiente climatizado, com temperatura de 20ºC ± 2ºC.")
        tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,75,527)
        tex = Paragraph("4. O pagamento deverá ser realizado conforme proposta.")
        tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,75,514.5)
        tex = Paragraph("5. Boletos pagos em atraso sofrerão ajustes de multas de juros e mora dia.")
        tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,75,502)
        tex = Paragraph(r"6. Fica convencionado entre as partes que em caso de desistência voluntária(após formalização da contratação) a parte culpada , incorrerá além das penalidades legais cabíveis, em multa compensatória de 40%(quarenta por cento) sobre o valor desta proposta, além de quaisquer outras custas com combinações legais.")
        tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,75,464.5) 
        tex = Paragraph("7. ***Não nos responsabilizamos por mercadorias na mão das transportadoras***")
        tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,75,452)
        tex = Paragraph("8. A manutenção do produto junto ao nosso estabelecimento não configura nenhuma forma de depósito.")
        tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,75,439.5)
        tex = Paragraph("9. O consumidor autoriza prévia e expressamente a venda do(s) produto(s) após 90 dias da conclusão dos serviços, para o pagamento dos serviços efetuados, tendo direito ao recebimento de eventual saldo positivo e tendo o dever de efetuar o pagamento da diferença restante, conforme o valor apurado com a venda do produto e o seu débito.")
        tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,75,393)
        tex = Paragraph("10. Fica o consumidor desde já ciente que os títulos gerados, provenientes destes orçamento podem ser executados judicialmente como forma de garantia de seu pagamento.")
        tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,75,367.5)
        tex = Paragraph("11. Em caso de extravio ou reimpressão de Certificado será cobrado o valor de R$ 5,00 (cinco reais) por segunda via emitida >>")
        tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,75,345.5)
        tex = Paragraph("12. Informar quanto a forma de disponibilização de certificado se físico ou digital. Quando não informado enviaremos apenas cópia digital.")
        tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,75,321.5)
        tex = Paragraph(r"13. Nas solicitações de prioridade ou urgência para calibrações, será cobrado além do valor orçado, a título de taxa de urgência, 30% a mais do valor de calibração do instrumento")
        tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,75,299.5)

        pdf.setFontSize(9)
        pdf.drawCentredString(125,285,'Horário de funcionamento')
        pdf.drawCentredString(179,270,'8:00 às 12:00 13:30 as 18:00 segunda a quinta-feira')
        pdf.drawCentredString(155,255,'8:00 às 12:00 13:30 as 17:00 sexta-feira ')

        tex = Paragraph("Em caso de FRETE RETORNO:PARA ESTE ITEM NÃO SERÁ EMITIDO NOTA FISCAL, POIS NÃO FAZ PARTE DA RECEITA TRIBUTÁRIA DA LEMPE. ")
        tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,70,230)
        tex = Paragraph("Favor informar até a aprovação do mesmo caso necessite de boletos separados quanto ao valor do frete e o valor dos serviços oferecidos pela LEMPE.")
        tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,70,205)
        pdf.drawInlineImage(
            r'static/img/assinatura.png',
            135, 0,
            preserveAspectRatio=True
        )
    def calcular_larguras_colunas(data, pdf):
        larguras = []
        
        for coluna in zip(*data):
            if any('\n' in str(valor) for valor in coluna):
                largura_maxima = max(pdf.stringWidth(str(valor), 'Helvetica', 10) for valor in coluna)
                larguras.append(largura_maxima)  # Adicione uma margem para melhorar a aparência
            else:
                largura_maxima = max(pdf.stringWidth(str(valor), 'Helvetica', 10) for valor in coluna)
                larguras.append(largura_maxima + 15)  # Adicione uma margem para melhorar a aparência
        
        return larguras
    def segunda_parte_pdf():
        pdf.showPage()
        pdf.drawInlineImage(
            r'static/img/Imagem - de cima.jpeg',
            50, 700,
            preserveAspectRatio=True
        )
        pdf.setFontSize(15)
        pdf.setFillColor(colors.black)
        pdf.drawCentredString(480,734,'Orçamento nº: {}/{}'.format(orcamento.orcamento_raiz, ano_atual))
        pdf.setFontSize(9)
        tex = Paragraph("Os equipamentos/instrumentos enviados para calibração em nossos laboratórios devem vir acompanhados de TODOS OS ACESSORIOS. Se por ventura a falta de algum acessório impedir a calibração ou manutenção do equipamento e ou instrumento, a responsabilidade do envio é do cliente e todos os custos de envio e coleta relacionados também.")
        tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,70,650)
        pdf.setFont("Helvetica-Bold",9)
        pdf.drawCentredString(165,625,'3 - ESCOPO PARA PRESTAÇÃO DE SERVIÇOS')
        
        # Definindo o cabeçalho da tabela fora do loop
        if orcamento.tipo_de_desconto == 'porcentagem':
            cabecalho = ['Item', 'Descrição', 'Local', 'Serviço', 'Prazo de \nEntrega', 'Valor \nUnitário', 'Desconto (%)', 'Acréscimo', 'Valor \nTotal']
        elif orcamento.tipo_de_desconto == 'valor_real':
            cabecalho = ['Item', 'Descrição', 'Local', 'Serviço', 'Prazo de \nEntrega', 'Valor \nUnitário', 'Desconto (R$)', 'Acréscimo', 'Valor \nTotal']
        else:
            cabecalho = ['Item', 'Descrição', 'Local', 'Serviço', 'Prazo de \nEntrega', 'Valor \nUnitário', 'Desconto', 'Acréscimo', 'Valor \nTotal']

        # Adicionando o cabeçalho à lista de dados
        data = [cabecalho]

        # Iterando sobre cada objeto Servico na lista servico
        for servico_obj in servico:
            prazo = orcamento.validade_proposta.strftime('%d/%m/%Y') if orcamento and orcamento.validade_proposta else 'N/A'
            descricao = str(servico_obj.descricao) if servico_obj and servico_obj.descricao else 'N/A'
            local = str(servico_obj.local) if servico_obj and servico_obj.local else 'N/A'
            id_equip = str(servico_obj.id) if servico_obj and servico_obj.id else 'N/A'
            tipo_orcamento = str(orcamento.tipo_orcamento) if orcamento and orcamento.tipo_orcamento else 'N/A'
            valor_unitario = str(servico_obj.valor) if servico_obj and servico_obj.valor else 0
            desconto = float(orcamento.desconto) if orcamento and orcamento.desconto else 0
            acrescimo = float(orcamento.acrescimo) if orcamento and orcamento.acrescimo else 0
            total = sum(float(servico.valor) for servico in servico) if servico else 0

            if orcamento.tipo_de_desconto == 'porcentagem':
                valor_desconto = (desconto / 100) * total
                total -= valor_desconto
            elif orcamento.tipo_de_desconto == 'valor_real':
                total -= desconto

            total += acrescimo

            total = str(total)
            
            # Adicionando os dados de cada serviço à lista de dados
            data.append([id_equip, descricao, local, tipo_orcamento, prazo, 'R$ {}'.format(valor_unitario), '{}'.format(desconto), 'R$ {}'.format(acrescimo), 'R$ {}'.format(total)])

        # Construindo a tabela com os dados
        larguras_colunas = calcular_larguras_colunas(data, pdf)
        tabela = Table(data, colWidths=larguras_colunas, rowHeights=30, style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])

        # Posicionando a tabela no PDF
        tabela.wrapOn(pdf, 500, 200)
        tabela.drawOn(pdf, 15, 360)

        pdf.showPage()
        pdf.drawInlineImage(
                r'static/img/Imagem - de cima.jpeg',
                50, 700,
                preserveAspectRatio=True
            )

        # Desenhar o texto centralizado com a fonte definida
        pdf.drawCentredString(130, 545, '4 - CONDIÇÕES COMERCIAIS:')    
        pdf.setFontSize(8)

        pdf.drawCentredString(130, 535, 'Condições de Pagamento:')
        pdf.drawCentredString(210, 535, str(orcamento.condicao_pagamento) if orcamento and orcamento.condicao_pagamento else 'N/A')

        pdf.drawCentredString(123, 525, 'Forma de Pagamento:')
        pdf.drawCentredString(210, 525, str(orcamento.forma_pagamento) if orcamento and orcamento.forma_pagamento else 'N/A')

        pdf.drawCentredString(103, 515, 'Certificado:')
        pdf.drawCentredString(210, 515, 'Certificado Digital')

        observacao = str(orcamento.observacoes) if orcamento and orcamento.observacoes else 'Sem observações'
        pdf.drawCentredString(106, 505, 'Observações:')
        tex = Paragraph(observacao)
        tex.wrapOn(pdf,500,200)
        tex.drawOn(pdf,95,490)
        pdf.setFont("Helvetica-Bold",9)
        pdf.drawCentredString(140,450,'5 - APROVAÇÃO DO ORÇAMENTO:')
        data = [
        ['Nome', 'Setor', 'Data', 'Assinatura'],
        ['', '', '', ''], 
        ]

        # Criar Tabela
        larguras_colunas = calcular_larguras_colunas(data, pdf)
        tabela = Table(data, colWidths=142, rowHeights=20, style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])
        # Posicionar a Tabela
        tabela.wrapOn(pdf, 500, 200)
        tabela.drawOn(pdf, 20, 400)

        tex = Paragraph(r"Local do Serviço:")
        tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,70,370)

        if orcamento and orcamento.local:
            if orcamento.local == 'LEMPE':
                pdf.drawCentredString(155, 375, 'X')
            elif orcamento.local == 'In Loco':
                pdf.drawCentredString(225, 375, 'X')
            else:
                pass

        # Desenha a caixa "LEMPE"
        pdf.rect(150, 370, 15, 15)  # posição x, posição y, largura, altura
        pdf.drawString(170, 370, "LEMPE")

        # Desenha a caixa "In Loco"
        pdf.rect(220, 370, 15, 15)
        pdf.drawString(240, 370, "In Loco")


        pdf.drawInlineImage(
            r'static/img/assinatura.png',
            135, 0,
            preserveAspectRatio=True
        )


        

    # Call the functions with the data from the form
    primeira_parte_pdf(pdf)
    segunda_parte_pdf()
    

    # Save the PDF and prepare the response
    pdf.showPage()
    pdf.drawInlineImage(
            r'static/img/Imagem - de cima.jpeg',
            50, 700,
            preserveAspectRatio=True
        )
    pdf.setFontSize(15)
    pdf.setFillColor(colors.black)
    pdf.drawCentredString(480,734,'Orçamento nº: {}/{}'.format(orcamento.orcamento_raiz, ano_atual))
    
    pdf.setFont("Helvetica-Bold",9)
    pdf.drawCentredString(315,700,'INFORMAÇÕES PARA ORIENTAÇÃO AO CLIENTE')

    pdf.setFontSize(6)

    tex = Paragraph(r"1.0 - Serviços de Calibração:")
    tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,70,675)
    tex = Paragraph(r"1.1 - Calibração interna (Realizada nas instalações da CONTRATADA)")
    tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,70,665)
    tex = Paragraph(r"1.2 - Prazo de atendimento:")
    tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,70,655)
    tex = Paragraph(r"O prazo para execução dos serviços internos será aquele ofertado na proposta comercial considerando dias úteis.")
    tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,70,630)
    tex = Paragraph(r"2.0 - Calibração externa (Realizada nas instalações do CLIENTE):")
    tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,70,615)
    tex = Paragraph(r"Agendamento: As calibrações realizadas nas instalações dos clientes serão agendadas com o mesmo. Os instrumentos e ou equipamentos devem estar disponíveis no dia agendado sob pena de ser cobrada uma multa por visita técnica improdutiva no valor de R$ 550,00 quinhentos e cinquenta reais. O agendamento pode ser cancelado com até 72 horas de antecedência.")
    tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,70,565)
    tex = Paragraph(r"3.0 - Código de identificação dos instrumentos(Tag):")
    tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,70,550)
    tex = Paragraph(r"O código de identificação é a 'Carteira de Identidade' do instrumento, caso seja fornecida a forma / lógica de identificação dos instrumentos a CONTRATADA dará sequência às codificações dos mesmos, sem a necessidade de que sejam especificados um a um. Caso Tag/ Código de Identificação do equipamento não seja informado será criado TAG aleatório definido pela LEMPE.")
    tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,70,500)
    tex = Paragraph(r"4.0 - Periodicidade da calibração:")
    tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,70,480)
    tex = Paragraph(r"A periodicidade possibilitará que a CONTRATADA faça o gerenciamento dos instrumentos e gere as etiquetas dos mesmos, de forma que o cliente seja informado com 30 dias de antecedência sobre o vencimento de seus instrumentos. A periodicidade deve ser informada no ato da aprovação da proposta comercial. Quando não informado pelo cliente será aplicado prazo de 12 meses.")
    tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,70,435)
    tex = Paragraph(r"5.0 - Critério de aceitação ou limite de erro permissível (opcional):")
    tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,70,420)
    tex = Paragraph(r"O critério de aceitação, possibilitará que conste no certificado de calibração um laudo de aprovação ou reprovação conforme critério do cliente. Caso esta informação não seja fornecida o certificado poderá ser emitido, porém sem a aprovação ou reprovação. Em caso de procedimento ou critério específico, o mesmo deverá ser informado antecipadamente para inclusão em orçamento e sistema.")
    tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,70,370)
    tex = Paragraph(r"6.0 - Procedimentos de Trabalhos Técnicos:")
    tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,70,355)
    tex = Paragraph(r"Os serviços de calibração e medição serão realizados conforme procedimentos internos do Laboratório. Caso queira tomar conhecimento do método utilizado favor entrar em contato com nosso gerente técnico. Não serão fornecidas cópias de nossos procedimentos técnicos de calibração. Caso o cliente não defina os pontos de calibração, a LEMPE definirá os mesmos em consonância com nossos procedimentos internos.")
    tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,70,310)
    tex = Paragraph(r"7.0 - Cópias dos certificados dos Padrões RBC:")
    tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,70,295)
    tex = Paragraph(r"A cópia dos certificados de calibrações RBC dos padrões utilizados estarão disponíveis para download no nosso site no endereço: w w w.lempe.com.br <http://w w w.lempe.com.br> , para ter acesso ao mesmo o usuário deve solicitar a permissão à contratada.")
    tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,70,260)
    tex = Paragraph(r"8.0 - Logística (Remessa e Retorno de mercadoria):")
    tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,70,245)
    tex = Paragraph(r"Frete de remessa e retorno por conta do cliente.")
    tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,70,235)
    tex = Paragraph(r"- O prazo de entrega não abrange o transporte do instrumento.")
    tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,70,225)
    tex = Paragraph(r"- É importante salientar que o transporte não é de responsabilidade da contratada. A contratada não se responsabilizará por qualquer dano ocorrido durante o mesmo. Caso o CONTRATANTE deseje incluir o frete de retorno na cobrança dos serviços, será cobrado além do valor do frete um percentual de 50% sobre o valor do frete para recompensa pelo serviço prestado.")
    tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,70,175)
    tex = Paragraph(r"9.0 - Serviços de Manutenção:")
    tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,70,155)
    tex = Paragraph(r"Uma vez aprovada a realização dos serviços, o departamento de manutenção procederá ao planejamento de execução dos serviços. Os nossos orçamentos de manutenção não contemplam a realização de serviços de calibração, sendo estes, objeto de orçamento específico. O faturamento será efetuado na data do término dos serviços de manutenção, com nota fiscal em separado da calibração. Os serviços de manutenção têm um período de garantia padrão de 30 dias, caso contrário, este prazo estará definido em nossa proposta técnico/comercial. No caso de aprovação da calibração após a execução dos serviços de manutenção, os equipamentos serão enviados diretamente ao nosso laboratório e, a partir dessa data, utilizará o sistema de funcionamento da calibração interna descrito no item 1.2. Os prazos de manutenção do equipamento podem variar de acordo com a disponibilidade de peças. Para grande quantidade de peças o prazo de entrega será atualizado em conformidade com corpo técnico e recebimento das remessas de equipamentos.")
    tex.wrapOn(pdf,500,200) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,70,35)
    




    
    pdf.save()

    # Prepare the response with the generated PDF
    with open(pdf_file_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="orçamento_{}/{}_{}.pdf"'.format(orcamento.orcamento_raiz, ano_atual, contato.name)

    return response



@require_http_methods(["GET"])
def buscar_informacoes_banco(request):
    try:

        data_do_banco = list(Contacts_Customers.objects.values())

        return JsonResponse(data_do_banco)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def buscar_contatos(request):
    if request.method == 'POST' and 'cliente' in request.POST:
        cliente_selecionado = request.POST['cliente']
        print(cliente_selecionado)
        contatos = Contacts_Customers.objects.filter(id_customer=cliente_selecionado)
        print(contatos)
        contatos_data = [{'id': contato.id, 'nome': contato.name} for contato in contatos]
        return JsonResponse({'contatos': contatos_data})
    else:
        return JsonResponse({'error': 'Método não permitido ou parâmetros ausentes'})
    
    
from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrcamentoForm

def orcamento_update_view(request, orcamento_id):
    orcamento = get_object_or_404(Orcamento, pk=orcamento_id)
    form = OrcamentoForm(request.POST or None, instance=orcamento)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Orçamento atualizado com sucesso!")
        return redirect("view-orcamento")
    else:
        print(form.errors)
    
    return render(request, 'orcamento_atualizar.html', {'form': form, 'orcamento': orcamento})




