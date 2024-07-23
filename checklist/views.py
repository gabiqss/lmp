from django.shortcuts import render, redirect, get_object_or_404
from .forms import ChecklistForm
from .models import Checklist
import json


def create_checklist(request):
    if request.method == 'POST':
        form = ChecklistForm(request.POST)

        if form.is_valid():
            checklist = form.save(commit=False)

            campos_dinamicos = []

            fieldCounter = 0

            while True:
                tipo = request.POST.get(f'tipo_{fieldCounter}')
                if tipo is None:
                    break

                informacao = request.POST.get(f'informacao_{fieldCounter}')
                if informacao == None:
                    informacao = 'Sem informações'
                descricao = request.POST.get(f'descricao_{fieldCounter}')
                
                opcoes = []
                opcoes_raw = request.POST.getlist(f'opcoes_{fieldCounter}[]')
                for opcao in opcoes_raw:
                    opcoes.append(opcao)

                campo = {
                    'tipo': tipo,
                    'informacao': informacao,
                    'descricao': descricao,
                    'opcoes': opcoes,
                }
                campos_dinamicos.append(campo)

                fieldCounter += 1

            if campos_dinamicos:
                checklist.campos_dinamicos = campos_dinamicos
                checklist.save()

            checklists = Checklist.objects.all()

            return render(request, 'main/consulta_checklists.html', {'checklists': checklists})

    else:
        form = ChecklistForm()

    return render(request, 'main/criar_checklist.html', {'form': form})



def checklist_list_view(request):
    checklists = Checklist.objects.all()
    return render(request, 'main/consulta_checklists.html', {'checklists': checklists})


def checklist(request, id):
    query = get_object_or_404(Checklist, pk=id)
    
    # Obtendo os dados da string JSON diretamente do campo campos_dinamicos
    dados_str = query.campos_dinamicos

    # Convertendo a string para um objeto Python
    dados_lista = json.loads(dados_str.replace("'", "\""))

    return render(request, 'main/checklists_id.html', {'query': dados_lista})
