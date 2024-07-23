from django import forms
from django.forms import ModelForm
from django.forms.widgets import DateInput
from instruments.models import InstrumentsInstruments
from main.models import Contacts_Customers, Customers_main
from padrao.models import Novo_Padrão
from django.core.exceptions import ValidationError
from orcamento.models import Orcamento, TipoOrcamento, Solicitacao, PagamentoCondicao, PagamentoForma, AnexosOrcamento, ServicosOrcamento, ServicoCalibracao, ServicoEnsaio, ServicoManutencao, ServicoQT, OrcamentoAtividade, AnexosOrcamentoAtividade, ServicosOrcamentoAtividade





class OrcamentoForm(ModelForm):
    forma_solicitacao = forms.ModelChoiceField(queryset=Solicitacao.objects.all(), widget=forms.Select(attrs={"class": "form-control select2", "placeholder": "Solicitação"}))
    condicao_pagamento = forms.ModelChoiceField(queryset=PagamentoCondicao.objects.all(), widget=forms.Select(attrs={"class": "form-control select2", "placeholder": "Condição de pagamento"}))
    forma_pagamento = forms.ModelChoiceField(queryset=PagamentoForma.objects.all(), widget=forms.Select(attrs={"class": "form-control select2", "placeholder": "Forma de pagamento"}))
    tipo_orcamento = forms.ModelChoiceField(queryset=TipoOrcamento.objects.all(), widget=forms.Select(attrs={"class": "form-control select2", "placeholder": "Tipo de orçamento"}))
    solicitante = forms.ModelChoiceField(queryset=Customers_main.objects.all(), widget=forms.Select(attrs={"class": "form-control select2", "placeholder": "Solicitante"}))
    contato = forms.ModelChoiceField(queryset=Contacts_Customers.objects.all(), widget=forms.Select(attrs={"class": "form-control select2", "placeholder": "Contato"}))
    validade_proposta = forms.DateTimeField(widget=forms.DateInput(attrs={"class": "form-control", "type":"date"}))
    data_cadastro = forms.DateTimeField(widget=forms.DateInput(attrs={"class": "form-control", "type":"date"}))
    local_choices = (
        ("LEMPE", "LEMPE"),
        ("In Loco", "In Loco"),
    )

    contrato_choices = (
        ("Sim", "Sim"),
        ("Não", "Não"),
    )
    local = forms.ChoiceField(choices=local_choices, widget=forms.Select(attrs={"class": "form-control select2", "placeholder": "Local"}))
    contrato = forms.ChoiceField(choices=contrato_choices, widget=forms.Select(attrs={"class": "form-control select2", "placeholder": "Contrato"}))
    tipo_de_desconto_choices = (
        ("porcentagem", "Porcentagem"),
        ("valor_real", "Valor real"),
    )
    tipo_de_desconto = forms.ChoiceField(choices=tipo_de_desconto_choices, widget=forms.Select(attrs={"class": "form-control select2", "placeholder": "Tipo de desconto"}))
    status_choices = (
        ("Aberto", "Aberto"),
        ("Fechado", "Fechado"),
        ("Cancelado", "Cancelado"),
    )
    status = forms.ChoiceField(choices=status_choices, widget=forms.Select(attrs={"class": "form-control select2", "placeholder": "Status"}))
    class Meta:
        model = Orcamento
        fields = "__all__"
        exclude = []
        labels = {
            "solicitante": "Solicitante",
            "contato": "Contato",
            "responsavel": "Responsável",
            "validade_proposta": "Validade da proposta",
            "forma_pagamento": "Forma de pagamento",
            "condicao_pagamento": "Condição de pagamento",
            "tipo_orcamento": "Tipo de orçamento",
            "forma_solicitacao": "Como foi solicitado",
            "observacoes": "Observações",
            "contrato": "Contrato",
            "local": "Local",
            "acrescimo": "Acréscimo",
            "desconto": "Desconto",
            "tipo_de_desconto": "Tipo de desconto",
            "status": "Status",
            "orcamento_raiz": "Orcamento raiz"
        }
        widgets = {
            "solicitante": forms.Select(attrs={"class": "form-control select2"}),
            "contato": forms.Select(attrs={"class": "form-control select2"}),
            "responsavel": forms.Select(attrs={"class": "form-control select2"}),
            "forma_pagamento": forms.Select(attrs={"class": "form-control select2", "placeholder": "Forma de pagamento"}),
            "condicao_pagamento": forms.Select(attrs={"class": "form-control select2", "placeholder": "Condição"}),
            "tipo_orcamento": forms.Select(attrs={"class": "form-control select2", "placeholder": "Observações"}),
            "forma_solicitacao": forms.Select(attrs={"class": "form-control select2", "placeholder": "Solicitação", "choices": "orcamento.Solicitacao"}),
            "observacoes": forms.Textarea(attrs={"class": "form-control", "rows": 3, "cols": 4, "style": "resize:none", "placeholder": "Observações"}),
            "acrescimo": forms.TextInput(attrs={"class": "form-control"}),
            "desconto": forms.TextInput(attrs={"class": "form-control"}),
            

            
        }
    
            

class OrcamentoTipoForm(ModelForm):
    class Meta:
        model = TipoOrcamento
        fields = ["tipo"]
        labels = {
            "tipo": "Tipo de orçamento*",
        }
        widgets = {
            "tipo": forms.TextInput(attrs={"class": "form-control"}),
        }

class SolicitacaoForm(ModelForm):
    class Meta:
        model = Solicitacao
        fields = ["meio_solicitacao"]
        labels = {
            "meio_solicitacao": "Solicitação*",
        }
        widgets = {
            "meio_solicitacao": forms.TextInput(attrs={"class": "form-control"}),
        }

class PagamentoCondicaoForm(ModelForm):
    class Meta:
        model = PagamentoCondicao
        fields = ["condicao"]
        labels = {
            "condicao": "Condição de pagamento*",
        }
        widgets = {
            "condicao": forms.TextInput(attrs={"class": "form-control"}),
        }

class PagamentoFormaForm(ModelForm):
    class Meta:
        model = PagamentoForma
        fields = ["forma"]
        labels = {
            "forma": "Forma de pagamento*",
        }
        widgets = {
            "forma": forms.TextInput(attrs={"class": "form-control"}),
        }

class AnexosOrcamentoForm(ModelForm):
    class Meta:
        model = AnexosOrcamento
        fields = ["anexo"]
        labels = {
            "anexo": "Anexo*",
        }
        widget = {
            "anexo": forms.FileInput(attrs={"class": "form-control"}),
        }

class ServicoCalibracaoForm(ModelForm):
    class Meta:
        model = ServicoCalibracao
        fields = "__all__"
        labels = {
            "codigo": "Código*",
            "area_acreditacao": "Area de acreditação*",
            "especificacao": "Especificação*",
            "tipo_calibracao": "Tipo de calibração*",
            "tipo_item": "Tipo de item*",
            "local": "Local*",
            "descricao": "Descrição*",
            "pontos": "Pontos*",
            "pontos_valor_adicional": "Pontos com valor adicional*",
            "valor": "Valor*",
        }
        widgets = {
            "codigo": forms.TextInput(attrs={"class": "form-control"}),
            "area_acreditacao": forms.TextInput(attrs={"class": "form-control"}),
            "especificacao": forms.TextInput(attrs={"class": "form-control"}),
            "tipo_calibracao": forms.TextInput(attrs={"class": "form-control"}),
            "tipo_item": forms.TextInput(attrs={"class": "form-control"}),
            "local": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.TextInput(attrs={"class": "form-control"}),
            "pontos": forms.TextInput(attrs={"class": "form-control"}),
            "pontos_valor_adicional": forms.TextInput(attrs={"class": "form-control"}),
            "valor": forms.TextInput(attrs={"class": "form-control"}),
        }

class ServicoManutencaoForm(ModelForm):
    class Meta:
        model = ServicoManutencao
        fields = "__all__"
        labels = {
            "codigo": "Código*",
            "area_acreditacao": "Area de acreditação*",
            "especificacao": "Especificação*",
            "tipo_servico": "Tipo de serviço*",
            "local": "Local*",
            "descricao": "Descrição*",
            "valor": "Valor*",
        }
        widgets = {
            "codigo": forms.TextInput(attrs={"class": "form-control"}),
            "area_acreditacao": forms.TextInput(attrs={"class": "form-control"}),
            "especificacao": forms.TextInput(attrs={"class": "form-control"}),
            "tipo_servico": forms.TextInput(attrs={"class": "form-control"}),
            "local": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.TextInput(attrs={"class": "form-control"}),
            "valor": forms.TextInput(attrs={"class": "form-control"}),
        }

class ServicoEnsaioForm(ModelForm):
    class Meta:
        model = ServicoEnsaio
        fields = "__all__"
        labels = {
            "codigo": "Código*",
            "area_acreditacao": "Area de acreditação*",
            "especificacao": "Especificação*",
            "tipo_servico": "Tipo de serviço*",
            "local": "Local*",
            "descricao": "Descrição*",
            "valor": "Valor*",
        }
        widgets = {
            "codigo": forms.TextInput(attrs={"class": "form-control"}),
            "area_acreditacao": forms.TextInput(attrs={"class": "form-control"}),
            "especificacao": forms.TextInput(attrs={"class": "form-control"}),
            "tipo_servico": forms.TextInput(attrs={"class": "form-control"}),
            "local": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.TextInput(attrs={"class": "form-control"}),
            "valor": forms.TextInput(attrs={"class": "form-control"}),
        }

class ServicoQTForm(ModelForm):
    class Meta:
        model = ServicoQT
        fields = "__all__"
        labels = {
            "codigo": "Código*",
            "area_acreditacao": "Area de acreditação*",
            "especificacao": "Especificação*",
            "tipo_servico": "Tipo de serviço*",
            "local": "Local*",
            "descricao": "Descrição*",
            "valor": "Valor*",
        }
        widgets = {
            "codigo": forms.TextInput(attrs={"class": "form-control"}),
            "area_acreditacao": forms.TextInput(attrs={"class": "form-control"}),
            "especificacao": forms.TextInput(attrs={"class": "form-control"}),
            "local": forms.TextInput(attrs={"class": "form-control"}),
            "tipo_servico": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.TextInput(attrs={"class": "form-control"}),
            "valor": forms.TextInput(attrs={"class": "form-control"}),
        }

class ServicosOrcamentoForm(ModelForm):
    class Meta:
        model = ServicosOrcamento
        fields = "__all__"
        labels = {
            "codigo": "Código*",
            "area_acreditacao": "Area de acreditação*",
            "especificacao": "Especificação*",
            "tipo_servico": "Tipo de serviço*",
            "local": "Local*",
            "descricao": "Descrição*",
            "valor": "Valor*",
        }
        widgets = {
            "codigo": forms.TextInput(attrs={"class": "form-control"}),
            "area_acreditacao": forms.TextInput(attrs={"class": "form-control"}),
            "especificacao": forms.TextInput(attrs={"class": "form-control"}),
            "local": forms.TextInput(attrs={"class": "form-control"}),
            "tipo_servico": forms.TextInput(attrs={"class": "form-control"}),
            "tipo_calibracao": forms.TextInput(attrs={"class": "form-control"}),
            "tipo_item": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.TextInput(attrs={"class": "form-control"}),
            "pontos": forms.TextInput(attrs={"class": "form-control"}),
            "pontos_valor_adicional": forms.TextInput(attrs={"class": "form-control"}),
            "valor": forms.TextInput(attrs={"class": "form-control"}),
        }

class OrcamentoAtividadeForm(ModelForm):
    forma_solicitacao = forms.ModelChoiceField(queryset=Solicitacao.objects.all(), widget=forms.Select(attrs={"class": "form-control select2", "placeholder": "Solicitação", "label": "Forma de solicitação"}))
    condicao_pagamento = forms.ModelChoiceField(queryset=PagamentoCondicao.objects.all(), widget=forms.Select(attrs={"class": "form-control select2", "placeholder": "Condição de pagamento"}))
    forma_pagamento = forms.ModelChoiceField(queryset=PagamentoForma.objects.all(), widget=forms.Select(attrs={"class": "form-control select2", "placeholder": "Forma de pagamento"}))
    tipo_orcamento = forms.ModelChoiceField(queryset=TipoOrcamento.objects.all(), widget=forms.Select(attrs={"class": "form-control select2", "placeholder": "Tipo de orçamento", "type": "select"}))
    solicitante = forms.ModelChoiceField(queryset=Customers_main.objects.all(), widget=forms.Select(attrs={"class": "form-control select2", "placeholder": "Solicitante"}))
    contato = forms.ModelChoiceField(queryset=Contacts_Customers.objects.all(), widget=forms.Select(attrs={"class": "form-control select2", "placeholder": "Contato"}))
    validade_proposta = forms.DateTimeField(widget=forms.DateInput(attrs={"class": "form-control", "type":"date"}))
    data_cadastro = forms.DateTimeField(widget=forms.DateInput(attrs={"class": "form-control", "type":"date"}))
    local_choices = (
        ("LEMPE", "LEMPE"),
        ("In Loco", "In Loco"),
    )

    contrato_choices = (
        ("Sim", "Sim"),
        ("Não", "Não"),
    )
    local = forms.ChoiceField(choices=local_choices, widget=forms.Select(attrs={"class": "form-control select2", "placeholder": "Local"}))
    contrato = forms.ChoiceField(choices=contrato_choices, widget=forms.Select(attrs={"class": "form-control select2", "placeholder": "Contrato"}))
    tipo_de_desconto_choices = (
        ("porcentagem", "Porcentagem"),
        ("valor_real", "Valor real"),
    )
    tipo_de_desconto = forms.ChoiceField(choices=tipo_de_desconto_choices, widget=forms.Select(attrs={"class": "form-control select2", "placeholder": "Tipo de desconto", "label": "Tipo de desconto"}))
    class Meta:
        model = OrcamentoAtividade
        fields = "__all__"
        exclude = ["status", "orcamento", "responsavel_atividade"]
        
        widgets = {
            "solicitante": forms.Select(attrs={"class": "form-control select2"}),
            "contato": forms.Select(attrs={"class": "form-control select2"}),
            "responsavel": forms.Select(attrs={"class": "form-control select2"}),
            "validade_proposta": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            
            "condicao_pagamento": forms.Select(attrs={"class": "form-control select2", "placeholder": "Condição", "type": "select"}),
            "tipo_orcamento": forms.Select(attrs={"class": "form-control select2", "placeholder": "Observações"}),
            "forma_solicitacao": forms.Select(attrs={"class": "form-control select2", "placeholder": "Solicitação", "choices": "orcamento.Solicitacao"}),
            "observacoes": forms.Textarea(attrs={"class": "form-control", "rows": 3, "cols": 4, "style": "resize:none", "placeholder": "Observações"}),
            "acrescimo": forms.TextInput(attrs={"class": "form-control"}),
            "desconto": forms.TextInput(attrs={"class": "form-control"}),
        }

class AnexosOrcamentoAtividadeForm(ModelForm):
    class Meta:
        model = AnexosOrcamentoAtividade
        fields = ["anexo"]
        labels = {
            "anexo": "Anexo*",
        }
        widget = {
            "anexo": forms.FileInput(attrs={"class": "form-control"}),
        }

class ServicosOrcamentoAtividadeForm(ModelForm):
    class Meta:
        model = ServicosOrcamentoAtividade
        fields = "__all__"
        labels = {
            "codigo": "Código*",
            "area_acreditacao": "Area de acreditação*",
            "especificacao": "Especificação*",
            "tipo_servico": "Tipo de serviço*",
            "local": "Local*",
            "descricao": "Descrição*",
            "valor": "Valor*",
        }
        widgets = {
            "codigo": forms.TextInput(attrs={"class": "form-control"}),
            "area_acreditacao": forms.TextInput(attrs={"class": "form-control"}),
            "especificacao": forms.TextInput(attrs={"class": "form-control"}),
            "local": forms.TextInput(attrs={"class": "form-control"}),
            "tipo_servico": forms.TextInput(attrs={"class": "form-control"}),
            "tipo_calibracao": forms.TextInput(attrs={"class": "form-control"}),
            "tipo_item": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.TextInput(attrs={"class": "form-control"}),
            "pontos": forms.TextInput(attrs={"class": "form-control"}),
            "pontos_valor_adicional": forms.TextInput(attrs={"class": "form-control"}),
            "valor": forms.TextInput(attrs={"class": "form-control"}),
        }