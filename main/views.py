from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from ordemS.consts import StatusOs
from .models import Customers_main, Contacts_Customers, AnexosCliente, Fornecedores, AnexosFornecedores
from django.core.paginator import Paginator
from .forms import Cadatrar_Clientes, Contatos_Clientes, EmpresaForm, Cadatrar_Clientes_CPF, AnexosClienteForm, FornecedoresForm, AnexosFornecedoresForm, FornecedoresCPFForm
from functions import consult_cnpj
from django.http import HttpResponse, JsonResponse
from ordemS.models import Dados, OrdemDeServico
import pandas as pd
from django.db.models import Q
import requests
from django.urls import reverse
from django.views import View

 

def render_main_screen(request):
    """
    Renders the main screen of the application.

    Retrieves data and renders the main screen template with the necessary context.

    Args:
        request: HttpRequest object.

    Returns:
        Rendered HTML page with data.
    """

    user = request.user
    if not user.is_authenticated:
        return redirect("login")
    df = pd.read_csv('staticfiles/data/sectors.csv')
    CHOICES_SETOR = [(i, i) for i in sorted(df['NAME'][2:].unique())]
    dados = OrdemDeServico.objects.all()
    if request.GET.get("setor"):
        dados = dados.filter(setor=request.GET.get("setor"))
    opened_os_count = dados.filter(status=StatusOs.OPEN).count()
    in_progress_os_count = dados.filter(status=StatusOs.IN_PROGRESS).count()
    canceled_os_count = dados.filter(status=StatusOs.CANCELED).count()
    completed_os_count = dados.filter(status=StatusOs.COMPLETED).count()

    return render(
        request,
        "pages/home.html",
        {
            "ordens": dados,
            "opened_os_count": opened_os_count,
            "in_progress_os_count": in_progress_os_count,
            "canceled_os_count": canceled_os_count,
            "completed_os_count": completed_os_count,
            "CHOICES_SETOR": CHOICES_SETOR,
        },
    )


# Função para mostrar lista de clientes
def clientes(request):
    """
    Renders the list of clients.

    Retrieves client data and renders the client list template with the necessary context.

    Args:
        request: HttpRequest object.

    Returns:
        Rendered HTML page with client list data.
    """

    formulario = Cadatrar_Clientes()
    barra_pesquisa = request.GET.get("search")
    dados = Customers_main.objects.all()

    if barra_pesquisa:
        dados = dados.filter(
            Q(name__icontains=barra_pesquisa) |
            Q(cnpj__icontains=barra_pesquisa) |
            Q(phone__icontains=barra_pesquisa) |
            Q(email__icontains=barra_pesquisa)
        )

    paginator = Paginator(dados, 20)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)
    conj_dict = {
        "page_obj": page_obj,
        "formulario": formulario,
        "barra_pesquisa": barra_pesquisa,
    }
    return render(request, "pages/clientes.html", conj_dict)


# Função para consultar empresa através do CNPJ
def consultar_empresa(request):
    """
    Consults a company using its CNPJ.

    Allows users to search for a company using its CNPJ, retrieves data from an external API, 
    and renders the company search template with the necessary context.

    Args:
        request: HttpRequest object.

    Returns:
        Rendered HTML page with company search data.
    """

    empresa = None
    show_search_button = True
    show_save_button = False
    formulario = Cadatrar_Clientes()
    anexo_form = AnexosClienteForm()
    barra_pesquisa = request.GET.get("search")
    dados = Customers_main.objects.all()

    if barra_pesquisa:
        dados = dados.filter(
            Q(name__icontains=barra_pesquisa) |
            Q(cnpj__icontains=barra_pesquisa) |
            Q(phone__icontains=barra_pesquisa) |
            Q(email__icontains=barra_pesquisa)
        )
    paginator = Paginator(dados, 20)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)
    if request.method == "POST":
        form = EmpresaForm(request.POST)
        if form.is_valid():
            cnpj = form.cleaned_data["cnpj"]
            url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
            response = requests.get(url)
            if response.status_code == 200 and response.json()["status"] != "ERROR":
                dados = response.json()
                empresa = {
                    "cnpj": dados["cnpj"],
                    "corporate_name": dados["nome"],
                    "name": dados["fantasia"],
                    "address": dados["logradouro"],
                    "phone": dados["telefone"],
                    "email": dados["email"],
                    "city": dados["municipio"],
                    "cep": dados["cep"],
                    "address_number": dados["numero"],
                    "address_complement": dados["complemento"],
                    "neighborhood": dados["bairro"],
                    "uf": dados["uf"],
                }
                show_search_button = False
                show_save_button = True
                if (
                    request.POST.get("action") == "save" and request.method == "POST"
                ):  # Verifica se o botão "Salvar" foi pressionado
                    new_empresa = {
                        "cnpj": form.cleaned_data["cnpj"],
                        "name": request.POST.get("name"),
                        "phone": request.POST.get("phone"),
                        "email": request.POST.get("email"),
                        "corporate_name": request.POST.get("corporate_name"),
                        "municipal_registration": request.POST.get(
                            "municipal_registration"
                        ),
                        "state_registration": request.POST.get("state_registration"),
                        "address": request.POST.get("address"),
                        "city": request.POST.get("city"),
                        "uf": request.POST.get("uf"),
                        "cep": request.POST.get("cep"),
                        "description": request.POST.get("description"),
                        "fax": request.POST.get("fax"),
                        "neighborhood": request.POST.get("neighborhood"),
                        "date_of_fundation": request.POST.get("date_of_fundation"),
                        "web_site": request.POST.get("web_site"),
                        "id_market_segment": request.POST.get("id_market_segment"),
                        "id_size": request.POST.get("id_size"),
                        "address_number": request.POST.get("address_number"),
                        "address_complement": request.POST.get("address_complement"),
                        "payment_day": request.POST.get("payment_day"),
                        "is_requestor_in_field": request.POST.get(
                            "is_requestor_in_field"
                        ),
                        "payment_venc": request.POST.get("payment_venc"),
                        "company_responsible": request.POST.get("company_responsible"),
                        "credit_or_debit_card": request.POST.get(
                            "credit_or_debit_card"
                        ),
                        "tipo_cliente": request.POST.get("tipo_cliente"),
                    }
                    nova_empresa = Customers_main.objects.create(
                        **new_empresa
                    )  # Cria uma nova instância de Empresa com os dados do formulário
                    nova_empresa.save()  # Salva a nova instância no banco de dados
                    anexo_form = AnexosClienteForm(request.POST, request.FILES, initial={'cliente': nova_empresa})
                    print(anexo_form.is_valid())
                    if anexo_form.is_valid():
                        for file in request.FILES.getlist('anexo'):
                            AnexosCliente.objects.create(
                                cliente=nova_empresa,
                                anexo=file
                            )
                    else:
                        pass
                    messages.success(request, "Cliente cadastrado com sucesso!")
                    # Construa a URL para a nova página com o ID recém-criado
                    new_contact_url = reverse("new-contact", kwargs={"id": nova_empresa.id})

                    # Redirecione para a nova página
                    return redirect(new_contact_url)
                form = Cadatrar_Clientes(initial=empresa)
    else: 
        form = EmpresaForm()
        print('teste',form.errors)

    context = {
        "form": form,
        "form_anexo": anexo_form,
        "empresa": empresa,
        "show_search_button": show_search_button,
        "show_save_button": show_save_button,
        "page_obj": page_obj,
        "formulario": formulario,
        "barra_pesquisa": barra_pesquisa,
    }
    return render(request, "pages/cadastrar_cliente.html", context)

def cadastrar_cliente_cpf(request):
    """
    Registers a new client using CPF.

    Renders the client registration form for CPF and handles form submission.

    Args:
        request: HttpRequest object.

    Returns:
        Rendered HTML page with client registration form for CPF.
    """

    form = Cadatrar_Clientes_CPF()
    anexo_form = AnexosClienteForm()
    if request.method == "POST":
        form = Cadatrar_Clientes_CPF(request.POST)
        if form.is_valid():
            cliente = form.save()
            anexo_form = AnexosClienteForm(request.POST, request.FILES, initial={'cliente': cliente})
            print(anexo_form.is_valid())
            if anexo_form.is_valid():
                for file in request.FILES.getlist('anexo'):
                    AnexosCliente.objects.create(
                        cliente=cliente,
                        anexo=file
                    )
            else:
                pass
            return redirect("/clientes")

    return render(request, "pages/cadastrar_cliente_cpf.html", {"form": form, "form_anexo": anexo_form})

def fornecedores(request):
    formulario = FornecedoresForm()
    barra_pesquisa = request.GET.get("search")
    dados = Fornecedores.objects.all()

    if barra_pesquisa:
        dados = dados.filter(
            Q(name__icontains=barra_pesquisa) |
            Q(cnpj__icontains=barra_pesquisa) |
            Q(cpf__icontains=barra_pesquisa) |
            Q(phone__icontains=barra_pesquisa) |
            Q(email__icontains=barra_pesquisa)
        )

    paginator = Paginator(dados, 20)
    page = request.GET.get("page")
    page_obj = paginator.get_page(page)
    conj_dict = {
        "page_obj": page_obj,
        "formulario": formulario,
        "barra_pesquisa": barra_pesquisa,
    }
    return render(request, "pages/fornecedores.html", conj_dict)

def cadastrar_fornecedor(request):
    form = FornecedoresForm()
    anexo_form = AnexosFornecedoresForm()
    if request.method == "POST":
        form = FornecedoresForm(request.POST)
        if form.is_valid():
            fornecedor = form.save()
            anexo_form = AnexosFornecedoresForm(request.POST, request.FILES, initial={'fornecedor': fornecedor})
            print(anexo_form.is_valid())
            if anexo_form.is_valid():
                for file in request.FILES.getlist('anexo'):
                    AnexosFornecedores.objects.create(
                        fornecedor=fornecedor,
                        anexo=file
                    )
            else:
                pass
            return redirect("/fornecedores")
        
    return render(request, "pages/cadastrar_fornecedor.html", {"form": form, "form_anexo": anexo_form})

def cadastrar_fornecedor_cpf(request):
    form = FornecedoresCPFForm()
    anexo_form = AnexosFornecedoresForm()
    if request.method == "POST":
        form = FornecedoresCPFForm(request.POST)
        if form.is_valid():
            fornecedor = form.save()
            anexo_form = AnexosFornecedoresForm(request.POST, request.FILES, initial={'fornecedor': fornecedor})
            print(anexo_form.is_valid())
            if anexo_form.is_valid():
                for file in request.FILES.getlist('anexo'):
                    AnexosFornecedores.objects.create(
                        fornecedor=fornecedor,
                        anexo=file
                    )
            else:
                pass
            return redirect("/fornecedores")
        
    return render(request, "pages/cadastrar_fornecedor_cpf.html", {"form": form, "form_anexo": anexo_form})

  # Função para verificação e cadastro de cliente
def cliente_view(request, id):
    """
    Displays details of a client.

    Retrieves details of a specific client and renders the client details template with the necessary context.

    Args:
        request: HttpRequest object.
        id: ID of the client.

    Returns:
        Rendered HTML page with client details.
    """

    cliente = get_object_or_404(Customers_main, pk=id)
    contatos = Contacts_Customers.objects.filter(id_customer=cliente)
    form = Cadatrar_Clientes(initial=cliente.__dict__)
    if request.method == "POST":
        form = Cadatrar_Clientes(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect("/clientes")

    return render(
        request,
        "pages/cliente_id.html",
        {"form": form, "cliente": cliente, "contatos": contatos, "id": id},
    )


# Função para edição de cliente

def cliente_edit(request, id):
    """
    Edits details of a client.

    Allows users to edit details of a specific client and renders the client edit template with the necessary context.

    Args:
        request: HttpRequest object.
        id: ID of the client.

    Returns:
        Rendered HTML page for editing client details.
    """

    cliente = get_object_or_404(Customers_main, pk=id)
    form = Cadatrar_Clientes(instance=cliente)
    if request.method == "POST":
        form = Cadatrar_Clientes(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente atualizado.")
            return render(
                request,
                "pages/cliente_id_edit.html",
                {
                    "form": form,
                    "cliente": cliente,
                    "id": id,
                    "url_cancel": reverse("clientes"),
                },
            )
        else:
            return render(
                request,
                "pages/cliente_id_edit.html",
                {"form": form, "id": id, "url_cancel": reverse("clientes")},
            )
    else:
        return render(
            request,
            "pages/cliente_id_edit.html",
            {
                "form": form,
                "messages": messages.get_messages(request),
                "id": id,
                "url_cancel": reverse("clientes"),
            },
        )


# Função para deletar cliente
    
def delete_cliente(request, id):
    """
    Deletes a client.

    Deletes a specific client from the database and redirects to the previous page.

    Args:
        request: HttpRequest object.
        id: ID of the client.

    Returns:
        Redirects to the previous page after deleting the client.
    """

    cliente = get_object_or_404(Customers_main, pk=id)
    cliente.delete()
    messages.warning(request, "Cliente removido.")
    return redirect(request.META.get("HTTP_REFERER", "/"))


# Função para cadastrar novo contato do cliente

def novo_contato(request, id):
    """
    Creates a new contact for a client.

    Renders the form for creating a new contact for a client and handles form submission.

    Args:
        request: HttpRequest object.
        id: ID of the client.

    Returns:
        Rendered HTML page with the form for creating a new contact.
    """

    if request.method == "POST":
        form = Contatos_Clientes(request.POST)
        if form.is_valid():
            contato = form.save(commit=False)
            customer = Customers_main.objects.get(id=id)
            contato.id_customer = customer
            contato.save()
            return redirect('/cliente/' + str(id))

        else:
            return render(request, "pages/novo_contato.html", {"form": form, "id": id})
    else:
        form = Contatos_Clientes()
        return render(
            request,
            "pages/novo_contato.html",
            {"form": form, "messages": messages.get_messages(request), "id": id},
        )


# Função para editar contato do cliente
    
def editar_contato(request, id_cliente, id_contato):
    """
    Edits details of a contact for a client.

    Allows users to edit details of a specific contact for a client and renders the contact edit template with the necessary context.

    Args:
        request: HttpRequest object.
        id_cliente: ID of the client.
        id_contato: ID of the contact.

    Returns:
        Rendered HTML page for editing contact details.
    """

    cliente = get_object_or_404(Customers_main, pk=id_cliente)
    contato = get_object_or_404(Contacts_Customers, pk=id_contato)
    if request.method == "POST":
        form = Contatos_Clientes(instance=contato, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Contato salvo com sucesso!")
            return render(
                request,
                "pages/cliente_id_edit.html",
                {
                    "form": form,
                    "cliente": cliente,
                    "contato": contato,
                    "id": id_cliente,
                    "url_cancel": reverse("view-cliente", kwargs={"id": id_cliente}),
                },
            )
        else:
            return render(
                request,
                "pages/cliente_id_edit.html",
                {
                    "form": form,
                    "cliente": cliente,
                    "contato": contato,
                    "id": id_cliente,
                    "url_cancel": reverse("view-cliente", kwargs={"id": id_cliente}),
                },
            )
    else:
        form = Contatos_Clientes(instance=contato)
        print(id_cliente)
        return render(
            request,
            "pages/cliente_id_edit.html",
            {
                "form": form,
                "cliente": cliente,
                "contato": contato,
                "id": id_cliente,
                "url_cancel": reverse("view-cliente", kwargs={"id": id_cliente}),
            },
        )


# Função para deletar contato do cliente
    
def delete_contato(request, id_cliente, id_contato):
    """
    Deletes a contact for a client.

    Deletes a specific contact for a client from the database and redirects to the previous page.

    Args:
        request: HttpRequest object.
        id_cliente: ID of the client.
        id_contato: ID of the contact.

    Returns:
        Redirects to the previous page after deleting the contact.
    """

    contato = get_object_or_404(Contacts_Customers, pk=id_contato)
    contato.delete()
    messages.success(request, "Contato removido.")
    return redirect(request.META["HTTP_REFERER"])


# Função para exibir os contatos do cliente

def exibir_contatos(request):
    """
    Displays contact details.

    Retrieves contact details entered by the user and displays them.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse with contact details displayed.
    """
    
    if request.method == "POST":
        nome = request.POST.get("nome")
        setor = request.POST.get("setor")
        ramal = request.POST.get("ramal")
        telefone_comercial = request.POST.get("telefone_comercial")
        celular = request.POST.get("celular")
        email = request.POST.get("email")
        data_nasc = request.POST.get("data_nasc")

        # Criar um dicionário para armazenar os dados de contato
        dados_contato = {
            "nome": nome,
            "setor": setor,
            "ramal": ramal,
            "telefone_comercial": telefone_comercial,
            "celular": celular,
            "email": email,
            "data_nasc": data_nasc,
        }

        # Exibir os valores cadastrados no terminal
        print(f"Nome: {nome}")
        print(f"Setor: {setor}")
        print(f"Ramal: {ramal}")
        print(f"Telefone Comercial: {telefone_comercial}")
        print(f"Celular: {celular}")
        print(f"E-mail: {email}")
        print(f"Data de Nascimento: {data_nasc}")

        return HttpResponse("<h1>Valores cadastrados exibidos no terminal!</h1>")
    else:
        return render(request, "main/exibir_contatos.html")

