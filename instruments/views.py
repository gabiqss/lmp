from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    InstrumentsInstruments,
    InstrumentTypes,
    InstrumentsModels,
    InstrumentsBands,
)
from main.models import Customers_main, CustomerSectors, Suppliers
from .forms import CadastroInstruments
from django.core.paginator import Paginator
from django.contrib import messages


import requests

# Função para cadastro de instrumentos


def cadastro_instrumento(request):
    customers = Customers_main.objects.values("id", "name").distinct()
    customers_sector = CustomerSectors.objects.values("id", "name").distinct()
    instrument_types = InstrumentTypes.objects.values("id", "nome").distinct()
    instrument_models = InstrumentsModels.objects.values("id", "name").distinct()
    instruments_Bands = InstrumentsBands.objects.values("id", "name").distinct()
    suppliers = Suppliers.objects.values("id", "name").distinct()

    if request.method == "POST":
        form = CadastroInstruments(request.POST)
        if form.is_valid():
            instrument = form.save(commit=False)
            id_customer = request.POST.get("id_customer")
            print(id_customer)
            if id_customer:
                instrument.id_customer = Customers_main.objects.get(id=int(id_customer))
                print(instrument.id_customer)
            id_customer_sector = request.POST.get("id_customer_sector")
            if id_customer_sector:
                instrument.id_current_sector = CustomerSectors.objects.get(
                    id=int(id_customer_sector)
                )

            id_instrument_type = request.POST.get("id_instrument_type")
            if id_instrument_type:
                instrument.id_instrument_type = InstrumentTypes.objects.get(
                    id=int(id_instrument_type)
                )

            id_instrument_model = request.POST.get("id_instrument_model")
            if id_instrument_model:
                instrument.id_instrument_model = InstrumentsModels.objects.get(
                    id=int(id_instrument_model)
                )

            id_supplier = request.POST.get("id_supplier")
            if id_supplier:
                instrument.id_supplier = Suppliers.objects.get(id=int(id_supplier))
            messages.success(request, "Equipamento cadastrado com sucesso!")
            instrument.save()
    else:
        form = CadastroInstruments()

    return render(
        request,
        "instruments/cadastro_instrumentos.html",
        {
            "form": form,
            "customers": customers,
            "customers_sector": customers_sector,
            "instrument_types": instrument_types,
            "instrument_models": instrument_models,
            "suppliers": suppliers,
            "instruments_Bands": instruments_Bands,
            "messages": messages.get_messages(request),
        },
    )


# Função para consultar instrumentos do cliente


def instrumento_cliente(request):
    customers = Customers_main.objects.all()
    selected_customer_name = "Cliente"  # Valor padrão para evitar o erro
    instruments = None

    id_cliente = request.GET.get("name")
    if id_cliente:
        selected_customer = Customers_main.objects.get(id=id_cliente)
        selected_customer_name = selected_customer.name
        instruments = InstrumentsInstruments.objects.filter(id_customer=id_cliente)

    paginator = None
    page_obj = None

    if instruments is not None:
        paginator = Paginator(
            instruments, 10
        )  # Dividindo em páginas com 10 instrumentos por página
        page_number = request.GET.get(
            "page"
        )  # Obtendo o número da página da query string
        page_obj = paginator.get_page(page_number)  # Obtendo o objeto da página atual

    context = {
        "customers": customers,
        "instruments": page_obj,
        "selected_customer_name": selected_customer_name,
    }

    return render(request, "instruments/instruments.html", context)





from django.views.generic import CreateView, ListView
from .models import InstrumentTypes, InstrumentsModels
from .forms import InstrumentTypeForm, InstrumentsModelsForm

class InstrumentTypeCreateView(CreateView):
    model = InstrumentTypes
    form_class = InstrumentTypeForm
    template_name = 'instruments/instrument_type_create.html'
    success_url = '/'  # URL para redirecionar após a criação

class InstrumentTypeListView(ListView):
    model = InstrumentTypes
    template_name = 'instruments/instrument_type_list.html'
    context_object_name = 'instrument_types'


class InstrumentsModelsView(CreateView):
    model = InstrumentsModels
    form_class = InstrumentsModelsForm
    template_name = 'instruments/instrument_model_create.html'
    success_url = '/'


class InstrumentModelListView(ListView):
    model = InstrumentsModels
    template_name = 'instruments/instrument_model_list.html'
    context_object_name = 'instrument_models'