import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from main.models import Customers_main, Contacts_Customers
from orcamento.consts import StatusOrcamentos
from orcamento.models import Orcamento
from ordemS.models import Dados, OrdemDeServico
from .forms import DadosForm, DadosFormEdit
from xhtml2pdf import pisa
from django.urls import reverse
from django.contrib import messages


def ordem_servico(request):
    selected_orcamento = None
    selected_equipamento = None
    equipamentos = None
    if request.method == "POST":
        form = OrdemDeServicoForm(request.POST, request.FILES)
        if form.is_valid():
            # Salvar os dados do formulário no banco de dados
            instancia_da_os = form.save()
            #contact = instancia_da_os.equipamento.orcamento.contato
            # Renderizar o template HTML com os dados do formulário
            template = get_template("ordemS/template_pdf.html")
            html = template.render({"dados_formulario": instancia_da_os})

            # Criar o nome exclusivo para o arquivo PDF
            nome_arquivo = f"formulario_{instancia_da_os.id}.pdf"

            # Definir o caminho de salvamento do arquivo PDF
            file_path = os.path.join(settings.MEDIA_ROOT, nome_arquivo)

            # Gerar o PDF usando o xhtml2pdf
            with open(file_path, "w+b") as file:
                pisa.CreatePDF(html, dest=file)

            # Atualizar o campo 'arquivo_pdf' no modelo
            instancia_da_os.arquivo_pdf = file_path
            instancia_da_os.save()
            messages.success(request, "Ordem de serviço cadastrada.")

            # Retornar o PDF como resposta
            with open(file_path, "rb") as file:
                response = HttpResponse(file.read(), content_type="application/pdf")
                response["Content-Disposition"] = f'filename="{nome_arquivo}"'
                return response
        else:
            print(form.errors)
    orcamentos = Orcamento.objects.filter(status=StatusOrcamentos.MADE_PAYMENT)
    #id_orcamento = request.GET.get("id_orcamento")
    #id_equipamento = request.GET.get("id_equipamento")
    return render(
            request,
            "ordemS/template_do_pdf.html",
            {
                "form": form,
                "orcamentos": orcamentos,
                #"equipamentos": equipamentos,
                "selected_orcamento": selected_orcamento,
                #"selected_equipamento": selected_equipamento,
                "messages": messages.get_messages(request),
            },
        )
#    '''if id_orcamento is not None and int(id_orcamento) != 0:
#        selected_orcamento = Orcamento.objects.get(id=id_orcamento)
#        equipamentos = Equipamento.objects.filter(orcamento__id=id_orcamento)
#    elif id_equipamento is not None and int(id_equipamento) != 0:
 #       selected_equipamento = Equipamento.objects.get(id=id_equipamento)
 #       selected_orcamento = selected_equipamento.orcamento
  #      form = OrdemDeServicoForm(initial={"equipamento_id": selected_equipamento.id})
   #        request,
    #        "ordemS/template_do_pdf.html",
     #       {
      #          "form": form,
       #         "orcamentos": orcamentos,
        #        #"equipamentos": equipamentos,
         #       "selected_orcamento": selected_orcamento,
          #      #"selected_equipamento": selected_equipamento,
           #     "messages": messages.get_messages(request),
            #},
        #)'''
    # if customer_id is not None and int(customer_id) != 0:
    #     selected_customer = Customers_main.objects.get(id=customer_id)
    #     selected_contacts = Contacts_Customers.objects.filter(
    #         id_customer_id=customer_id
    #     )
    #     form = DadosForm(
    #         initial={
    #             "cnpj": selected_customer.cnpj,
    #             "razao_social": selected_customer.name,
    #             "endereco": selected_customer.address,
    #             "cidade": selected_customer.city,
    #             "bairro": selected_customer.neighborhood,
    #             "cep": selected_customer.cep,
    #             "fone": selected_customer.phone,
    #             "fax": selected_customer.fax,
    #         }
    #     )
    # else:
    #     form = DadosForm()
    return render(
        request,
        "ordemS/template_do_pdf.html",
        {
            # "form": form,
            "orcamentos": orcamentos,
            #"equipamentos": equipamentos,
            "selected_orcamento": selected_orcamento,
            #"selected_equipamento": selected_equipamento,
            "messages": messages.get_messages(request),
        },
    )


def editar_ordem_servico(request, id):
    ordem_servico = get_object_or_404(OrdemDeServico, pk=id)
    if request.method == "POST":
        form = OrdemDeServicoEditForm(instance=ordem_servico, data=request.POST)
        if form.is_valid():
            # Salvar os dados do formulário no banco de dados
            dados_formulario = form.save()
            # Renderizar o template HTML com os dados do formulário
            template = get_template("ordemS/template_pdf.html")
            html = template.render({"dados_formulario": dados_formulario})

            # Criar o nome exclusivo para o arquivo PDF
            nome_arquivo = f"formulario_{id}.pdf"

            # Definir o caminho de salvamento do arquivo PDF
            file_path = os.path.join(settings.MEDIA_ROOT, nome_arquivo)

            # Gerar o PDF usando o xhtml2pdf
            with open(file_path, "w+b") as file:
                pisa.CreatePDF(html, dest=file)

            # Atualizar o campo 'arquivo_pdf' no modelo
            dados_formulario.arquivo_pdf = file_path
            dados_formulario.save()

            # # Retornar o PDF como resposta
            # with open(file_path, "rb") as file:
            #     response = HttpResponse(file.read(), content_type="application/pdf")
            #     response["Content-Disposition"] = f'filename="{nome_arquivo}"'
            #     return response
            messages.success(request, "Ordem de serviço atualizada.")
            return render(
                request,
                "ordemS/ordem_servico_edit.html",
                {
                    "form": form,
                    "id": id,
                },
            )
        else:
            print(form.errors)

            return render(
                request,
                "ordemS/ordem_servico_edit.html",
                {
                    "form": form,
                    "id": id,
                },
            )
    else:
        form = OrdemDeServicoEditForm(instance=ordem_servico)
        return render(
            request,
            "ordemS/ordem_servico_edit.html",
            {
                "form": form,
                "id": id,
                "messages": messages.get_messages(request),
            },
        )
