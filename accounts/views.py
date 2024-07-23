from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout as django_logout
from .forms import CustomUserCreationForm, CustomUserEditionForm, AnexosColaboradorForm
from .models import CustomUser, AnexosColaborador
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages


def registro(request):
    """
    Renderiza a página de registro de usuário e processa o formulário de registro.

    Esta view permite que novos usuários se registrem no sistema. Se o método da
    requisição for POST, ela valida o formulário de registro submetido. Se o
    formulário for válido, o usuário é criado e autenticado, e a página de clientes
    é exibida. Caso contrário, o formulário é renderizado novamente com mensagens
    de erro.

    Args:
        request (HttpRequest): O objeto HttpRequest representando a requisição HTTP.

    Returns:
        HttpResponse: O objeto HttpResponse com a página renderizada.
    """
    # English
    """
    Renders the user registration page and processes the registration form.

    This view allows new users to register in the system. If the request method
    is POST, it validates the submitted registration form. If the form is valid,
    the user is created and authenticated, and the clients page is displayed.
    Otherwise, the form is rendered again with error messages.

    Args:
        request (HttpRequest): The HttpRequest object representing the HTTP request.

    Returns:
        HttpResponse: The HttpResponse object with the rendered page.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/clientes')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})

def login_view(request):
    """
    Renderiza a página de login e processa o formulário de login.

    Esta view permite que usuários existentes façam login no sistema. Se o método da
    requisição for POST, ela tenta autenticar o usuário com as credenciais fornecidas.
    Se a autenticação for bem-sucedida, o usuário é redirecionado para a página de clientes.
    Caso contrário, a página de login é renderizada novamente com uma mensagem de erro.

    Args:
        request (HttpRequest): O objeto HttpRequest representando a requisição HTTP.

    Returns:
        HttpResponse: O objeto HttpResponse com a página renderizada.
    """
    # English
    """
    Renders the login page and processes the login form.

    This view allows existing users to log in to the system. If the request method
    is POST, it attempts to authenticate the user with the provided credentials.
    If the authentication is successful, the user is redirected to the clients page.
    Otherwise, the login page is rendered again with an error message.

    Args:
        request (HttpRequest): The HttpRequest object representing the HTTP request.

    Returns:
        HttpResponse: The HttpResponse object with the rendered page.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/clientes')
        else:
            # Adicione lógica para lidar com tentativas de login inválidas, por exemplo, exibindo uma mensagem de erro.
            # Add logic to handle invalid login attempts, e.g., displaying an error message.
            pass
    return render(request, 'login.html')

def profile(request):
    """
    Renderiza a página de perfil do usuário.

    Esta view exibe o perfil do usuário logado no sistema.

    Args:
        request (HttpRequest): O objeto HttpRequest representando a requisição HTTP.

    Returns:
        HttpResponse: O objeto HttpResponse com a página renderizada.
    """
    # English
    """
    Renders the user profile page.

    This view displays the profile of the user logged in to the system.

    Args:
        request (HttpRequest): The HttpRequest object representing the HTTP request.

    Returns:
        HttpResponse: The HttpResponse object with the rendered page.
    """
    user = CustomUser.objects.get(id=request.user.id)
    return render(request, 'profile.html', {'user': user})

def my_logout(request):
    """
    Realiza o logout do usuário.

    Esta view realiza o logout do usuário logado no sistema.

    Args:
        request (HttpRequest): O objeto HttpRequest representando a requisição HTTP.

    Returns:
        HttpResponse: O objeto HttpResponse com o redirecionamento para a página de login.
    """
    # English
    """
    Performs user logout.

    This view logs out the user logged in to the system.

    Args:
        request (HttpRequest): The HttpRequest object representing the HTTP request.

    Returns:
        HttpResponse: The HttpResponse object with redirection to the login page.
    """

    if request.method == 'POST':
        print("Logout iniciado")
        django_logout(request)
        print("Logout concluído")
    return redirect('login')

def colaboradores(request):
    """
    Renderiza a página de colaboradores.

    Esta view exibe a lista de colaboradores cadastrados no sistema.
    Ela também permite a pesquisa de colaboradores por nome, CPF, celular ou e-mail.

    Args:
        request (HttpRequest): O objeto HttpRequest representando a requisição HTTP.

    Returns:
        HttpResponse: O objeto HttpResponse com a página renderizada.
    """
    # English
    """
    Renders the collaborators page.

    This view displays the list of collaborators registered in the system.
    It also allows searching for collaborators by name, CPF, phone number, or email.

    Args:
        request (HttpRequest): The HttpRequest object representing the HTTP request.

    Returns:
        HttpResponse: The HttpResponse object with the rendered page.
    """

    formulario = CustomUserCreationForm()
    barra_pesquisa = request.GET.get("search")
    dados = CustomUser.objects.all()

    if barra_pesquisa:
        dados = dados.filter(
            Q(full_name__icontains=barra_pesquisa) |
            Q(cpf__icontains=barra_pesquisa) |
            Q(celular__icontains=barra_pesquisa) |
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
    return render(request, 'colaboradores.html', conj_dict)

def delete_colaborador(request, id):
    """
    Deleta um colaborador do sistema.

    Esta view exclui um colaborador do sistema com base no ID fornecido.

    Args:
        request (HttpRequest): O objeto HttpRequest representando a requisição HTTP.
        id (int): O ID do colaborador a ser excluído.

    Returns:
        HttpResponse: O objeto HttpResponse com o redirecionamento para a página de colaboradores.
    """
    # English
    """
    Deletes a collaborator from the system.

    This view deletes a collaborator from the system based on the provided ID.

    Args:
        request (HttpRequest): The HttpRequest object representing the HTTP request.
        id (int): The ID of the collaborator to be deleted.

    Returns:
        HttpResponse: The HttpResponse object with redirection to the collaborators page.
    """

    user = CustomUser.objects.get(id=id)
    user.delete()
    return redirect('colaboradores')

def create_colaborador(request):
    """
    Renderiza a página de criação de colaborador e processa o formulário de criação.

    Esta view permite a criação de um novo colaborador no sistema. Se o método da
    requisição for POST, ela valida o formulário de criação submetido. Se o
    formulário for válido, o colaborador é criado e a página de colaboradores
    é exibida. Caso contrário, o formulário é renderizado novamente com mensagens
    de erro.

    Args:
        request (HttpRequest): O objeto HttpRequest representando a requisição HTTP.

    Returns:
        HttpResponse: O objeto HttpResponse com a página renderizada.
    """
    # English
    """
    Renders the collaborator creation page and processes the creation form.

    This view allows creating a new collaborator in the system. If the request method
    is POST, it validates the submitted creation form. If the form is valid, the
    collaborator is created, and the collaborators page is displayed.
    Otherwise, the form is rendered again with error messages.

    Args:
        request (HttpRequest): The HttpRequest object representing the HTTP request.

    Returns:
        HttpResponse: The HttpResponse object with the rendered page.
    """

    anexo_form = AnexosColaboradorForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            anexo_form = AnexosColaboradorForm(request.POST, request.FILES, initial={'usuario': user})
            print(anexo_form.is_valid())
            if anexo_form.is_valid():
                for file in request.FILES.getlist('anexo'):
                    AnexosColaborador.objects.create(
                        usuario=user,
                        anexo=file
                    )
            else:
                pass
            return redirect('colaboradores')
    else:
        form = CustomUserCreationForm()
    return render(request, 'create_colaborador.html', {'form': form, 'form_anexo': anexo_form})

def edit_colaborador(request, id):
    """
    Renderiza a página de edição de colaborador e processa o formulário de edição.

    Esta view permite a edição das informações de um colaborador existente no sistema.
    Se o método da requisição for POST, ela valida o formulário de edição submetido.
    Se o formulário for válido, as informações do colaborador são atualizadas e a
    página de colaboradores é exibida. Caso contrário, o formulário é renderizado
    novamente com mensagens de erro.

    Args:
        request (HttpRequest): O objeto HttpRequest representando a requisição HTTP.
        id (int): O ID do colaborador a ser editado.

    Returns:
        HttpResponse: O objeto HttpResponse com a página renderizada.
    """
    # English
    """
    Renders the collaborator edition page and processes the edition form.

    This view allows editing the information of an existing collaborator in the system.
    If the request method is POST, it validates the submitted edition form.
    If the form is valid, the collaborator's information is updated, and the
    collaborators page is displayed. Otherwise, the form is rendered again with
    error messages.

    Args:
        request (HttpRequest): The HttpRequest object representing the HTTP request.
        id (int): The ID of the collaborator to be edited.

    Returns:
        HttpResponse: The HttpResponse object with the rendered page.
    """

    user = CustomUser.objects.get(id=id)
    if request.method == 'POST':
        form = CustomUserEditionForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('colaboradores')
    else:
        form = CustomUserCreationForm(instance=user)
    return render(request, 'edit_colaborador.html', {'form': form}) 

def colaborador_detail_view(request, id):       
    colaborador = CustomUser.objects.get(id=id)
    anexos = AnexosColaborador.objects.filter(usuario=colaborador)

    return render(
        request,
        "detalhes_colaborador.html",
        {"colaborador":colaborador, "anexos":anexos},
    )