from django.shortcuts import render
from main.models import Customers_main
from procedimentos.models import Dados_procedimento
from instruments.models import InstrumentsInstruments
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, Paragraph
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from calculos import calcular_resultados, calcular_trena
from ordemS.consts import StatusOs
from ordemS.models import OrdemDeServico
from padrao.models import Novo_Padrão
from procEletronicos.models import ValoresCalculos, Procedimento_eletronico
import pandas as pd
from django.conf import settings
import locale
from datetime import datetime

def tabela_view(request):
    os_abertas = OrdemDeServico.objects.filter(status=StatusOs.OPEN)
    resultados = None
    ordem_de_servico = None
    identificar_proc = None
    selected_instrument = None
    tipo_instrumento = None
    modelo_instrumento = None
    procedimentos = None
    fabricante = None
    novo_padrao = None
    valor = "0"
    campos = "0"
    valor2 = 0
    colunas = 0
    valor5 = 0
    valor6 = 0
    deriva = 0
    u_padrao = 0
    k = 0
    repeticao = "0"
    numeros = []

    if request.method == "POST":
        os_id = request.POST.get("id_os")
        if os_id is not None and int(os_id) != 0:
            ordem_de_servico = OrdemDeServico.objects.get(id=os_id)
            

        if ordem_de_servico:
            selected_instrument = ordem_de_servico.equipamento.peca
            tipo_instrumento = selected_instrument.id_instrument_type 
            modelo_instrumento = selected_instrument.id_instrument_model
            print('ola', modelo_instrumento)
            print('aqui', tipo_instrumento)
            identificar_proc = Procedimento_eletronico.objects.get(
                tipo_instrumento=tipo_instrumento
            )
            quantd_campos = ValoresCalculos.objects.get(
                procedimento=identificar_proc.id
            )
            procedimentos = Dados_procedimento.objects.get(
                
            )
            print(quantd_campos)

            quantd_campos.valores = quantd_campos.valores.strip("[]")
            quantd_campos.valores = quantd_campos.valores.split(", ")
            quantd_campos.valores = [
                valor.strip("'") for valor in quantd_campos.valores
            ]
            campos = quantd_campos.valores[0]
            print(campos)

            quantd_colunas = ValoresCalculos.objects.get(procedimento=identificar_proc.id)
            quantd_colunas.valores = quantd_colunas.valores.strip("[]")
            quantd_colunas.valores = quantd_colunas.valores.split(", ")
            quantd_colunas.valores = [
                valor.strip("'") for valor in quantd_colunas.valores
            ]
            colunas = quantd_colunas.valores[2]
            print(colunas)

            valor2 = quantd_campos.valores[1]

            novo_padrao = None
            try:
                novo_padrao = Novo_Padrão.objects.get(tipo_instrumento=tipo_instrumento)
                print(novo_padrao)
                faixas = novo_padrao.faixas.all()

                resolucoes = [faixa.resolucao for faixa in faixas]

                valor6 = sum(resolucao.valor for resolucao in resolucoes)
            except Novo_Padrão.DoesNotExist:
                valor6 = None
            except Exception as e:
                print(f"Exceção inesperada: {e}")
                valor6 = None
            else:
                print("Nenhum erro ocorreu no bloco try.")


            valor5 = quantd_campos.valores[3]
        valor = campos
        repeticao = colunas
        fabricante = novo_padrao.fabricante if novo_padrao else None
        print('fabricante', fabricante)
        print('resolucao', valor6)
        incerteza_do_arredondamento = valor6 / 2
        print(incerteza_do_arredondamento)
        if int(repeticao) > 0:
            resultado = ""
            for i in range(1, int(repeticao) + 1):
                resultado += str(i)
            repeticao = resultado


        if int(valor) > 0:
            resultado = ""
            for i in range(1, int(valor) + 1):
                resultado += str(i)
            valor = resultado

        num_linhas = []
        num_colunas = []
        for i in repeticao:
            linha = []
            coluna = []
            for j in range(1, len(valor) + 1):
                num_linha = request.POST.get(f"numero {j}.{i}")
                num_coluna = request.POST.get(f"numero {j}.{i}")
                print(f"Valor de num_linha para i={i} e j={j}: {num_linha}")
                print(f"Valor de num_coluna para i={i} e j={j}: {num_coluna}")
                if num_coluna:
                    coluna.append(float(num_coluna))
                else:
                    coluna.append(0.0)
                if num_linha:
                    linha.append(float(num_linha))
                else:
                    linha.append(0.0)

            num_colunas.append(coluna)
            num_linhas.append(linha)

        numeros = set()
        for coluna in num_colunas:
            for num in coluna:
                numeros.add(num)
        for linha in num_linhas:
            for num in linha:
                numeros.add(num)
        numeros = list(numeros)


        deriva = request.POST.get("deriva") or 0
        u_padrao = request.POST.get("u_padrao") or 0
        k = request.POST.get("k") or 0
        print('deriva', deriva)
        print('u_padrao', u_padrao)
        print('fator', k)



        print("Números: ", numeros)
        list_num = [numeros]
        print('lista: ', list_num[0])
        if numeros:
            resultados = calcular_resultados(numeros, valor2, valor6, valor5, deriva, u_padrao, k, incerteza_do_arredondamento)
            
            print(resultados)
        
        
    return render(
        request,
        "calibracao/balanca.html",
        {
            "resultados": resultados,
            "os_abertas": os_abertas,
            "ordem_de_servico": ordem_de_servico,
            "selected_instrument": selected_instrument,
            "valores": valor,
            "colunas": repeticao,
            "resolucao": valor6,
            "tipo_instrumento": tipo_instrumento,
            "modelo_instrumento": modelo_instrumento,
            
            "identificar_proc": identificar_proc,
            "procedimentos": procedimentos,
            "fabricante": fabricante,
            "novo_padrao": novo_padrao,
        },
    )





def gerar_pdf_view(request):
    # Configurar a localidade para tratar números com vírgulas
    locale.setlocale(locale.LC_NUMERIC, 'pt_BR.UTF-8')  # ou o local mais apropriado para o seu caso

    # Recupere os dados do formulário ou de onde você estiver obtendo os dados
    data = {
        'calibracao': float(request.POST.get("calibracao") or 0),
        'empresa': request.POST.get("customer.name") or '0', #ok
        'endereco': f'{request.POST.get("customer.address"), request.POST.get("customer.address_number"), request.POST.get("customer.neighborhood"), request.POST.get("customer.city"), request.POST.get("customer.address_complement")}',
        'solicitante': request.POST.get("customer.name") or '0', #ok
        'tag': request.POST.get("selected_instrument.tag") or '0',
        'codigo': request.POST.get("selected_instrument.code") or '0',
        'serial': request.POST.get("selected_instrument.serial_number") or '0',
        'fabricante': request.POST.get("selected_instrument.manufacturer") or '0',
        'modelo': request.POST.get("selected_instrument.model"),
        'dados': request.POST.get("dados_procedimento") or '0',
        'numeros': request.POST.get("resultados.numeros") or '0',
        'resultados_media': locale.atof(request.POST.get("resultados.media") or '0'),
        'resultados_desvio': locale.atof(request.POST.get("resultados.desvio_padrao_amostra") or '0'),
        'resultados_incerteza': locale.atof(request.POST.get("resultados.incerteza_menor") or '0'),
        'resultados_tendencia': locale.atof(request.POST.get("resultados.tendencia") or '0'),
        'resultados_inc_padrao': locale.atof(request.POST.get("resultados.incerteza_padrao_up") or '0'),
        'resultados_inc_comb': locale.atof(request.POST.get("resultados.incerteza_combinada") or '0'),
        'resultados_liberdade_veff': locale.atof(request.POST.get("resultados.grau_de_liberdade_veff") or '0'),
        'resultados_abrang': locale.atof(request.POST.get("resultados.fator_de_abrangencia9045") or '0'),
        'resultados_expand': locale.atof(request.POST.get("resultados.incerteza_expandida") or '0'),
        'resultados_empuxo': locale.atof(request.POST.get("resultados.empuxo_do_ar") or '0'),
        'resultados_estabilidade': locale.atof(request.POST.get("resultados.estabilidade_do_padrao") or '0'),
        'resultados_excentri': locale.atof(request.POST.get("resultados.excentricidade") or '0'),
        'temperatura': str(request.POST.get("temperatura") or '0'),
        'pressao_barometrica': str(request.POST.get("pressao") or '0'),
        'umidade_relativa': str(request.POST.get("umidade") or '0'),
        'faixa_de_indicacao': locale.atof(request.POST.get("faixa_de_indicacao") or '0'),
        'resolucao': locale.atof(request.POST.get("resolucao") or '0'),
        'faixa_de_calibracao': locale.atof(request.POST.get("faixa_de_calibracao") or '0'),
        'ordem_de_servico': request.POST.get("ordem_de_servico") or '0',
        'data_da_calibracao': request.POST.get("data_da_calibracao") or '0',
        'data_da_emissao': request.POST.get("data_da_emissao") or '0',
        # Adicione outros dados conforme necessário
    }
    print(data)
    ano_atual = datetime.now().year
    # Restaurar a localidade padrão
    locale.setlocale(locale.LC_NUMERIC, '')

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

        pdf.setFontSize(15)
        pdf.setFillColor(colors.black)
        pdf.drawCentredString(480,748,'CERTIFICADO DE CALIBRAÇÃO')
        pdf.setFontSize(9)
        pdf.drawCentredString(560,734,str(request.POST.get("calibracao"))) # argumentos(y,x,calibracao) 

        # Colocando os textos em negrito: 

        pdf.setFont("Helvetica-Bold",9)

        # Colocando titulos referentes aos dados: 

        pdf.setStrokeColor(colors.lightgrey)
        pdf.setLineWidth(18)
        pdf.line(48,690,600,690) # argumentos(y-inicial,x-inicial,y-final,x-final)
        pdf.setFontSize(9)
        pdf.drawCentredString(115,685,'1. Dados do Solicitante')


        pdf.drawCentredString(85,668,'Cliente:')

        # inserindo um texto nessa porra....
        texto = Paragraph(request.POST.get("customer.name")) # instanciando o paragrafo depois de importar a biblioteca
        texto.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
        texto.drawOn(pdf,125,666 ) # colocando o paragrafo no pdf.....


        pdf.drawCentredString(90,650,'Endereço:')
        endereco_parts = [
            request.POST.get("customer.address"),
            request.POST.get("customer.address_number"),
            request.POST.get("customer.neighborhood"),
            request.POST.get("customer.city"),
            request.POST.get("customer.address_complement")
        ]

        # Remove valores nulos ou vazios
        endereco_parts = [part for part in endereco_parts if part]

        endereco_formatado = ', '.join(endereco_parts)
        texto = Paragraph(endereco_formatado) # instanciando o paragrafo depois de importar a biblioteca
        texto.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
        texto.drawOn(pdf,125,646 ) # colocando o paragrafo no pdf.....

        pdf.drawCentredString(90,630,'Solicitante:')

        texto = Paragraph(request.POST.get("customer.name")) # instanciando o paragrafo depois de importar a biblioteca
        texto.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
        texto.drawOn(pdf,125,628 ) # colocando o paragrafo no pdf.....


        # 2 - DADOS DO INSTRUMENTO: 

        pdf.setStrokeColor(colors.lightgrey)
        pdf.setLineWidth(18)
        pdf.line(48,590,600,590) # argumentos(y-inicial,x-inicial,y-final,x-final)
        pdf.drawCentredString(146,585,'2. Dados do Instrumento Calibrado')

        pdf.drawCentredString(104,570,' Instrumento:     ')

        tex = Paragraph(request.POST.get("selected_instrument.tag")) # instanciando o paragrafo depois de importar a biblioteca
        tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,150,567 )

        pdf.drawCentredString(104,555,' Identificação:   ')

        tex = Paragraph(request.POST.get("selected_instrument.code")) # instanciando o paragrafo depois de importar a biblioteca
        tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,150,553 )


        pdf.drawCentredString(108,540,'  Número de Série: ')

        tex = Paragraph(request.POST.get("selected_instrument.serial_number")) # instanciando o paragrafo depois de importar a biblioteca
        tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,150,539)


        pdf.drawCentredString(100,525,' Modelo:          ')

        tex = Paragraph(request.POST.get("selected_instrument.model")) # instanciando o paragrafo depois de importar a biblioteca
        tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,150,525)


        pdf.drawCentredString(100,510,'  Fabricante:      ')

        tex = Paragraph(request.POST.get("novo_padrao.fabricante_id.name")) # instanciando o paragrafo depois de importar a biblioteca
        tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,150,510)

        pdf.drawCentredString(100,495,' Classe:          ')

        tex = Paragraph(str('0')) # instanciando o paragrafo depois de importar a biblioteca
        tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,150,495)

        pdf.drawCentredString(100,480,'e:               ')

        tex = Paragraph(str(request.POST.get("resultados.erro"))) # instanciando o paragrafo depois de importar a biblioteca
        tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,150,480)

        pdf.drawCentredString(400,570,'Localização:')

        tex = Paragraph(str(request.POST.get("identificar_proc.local"))) # instanciando o paragrafo depois de importar a biblioteca
        tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,470,570)


        pdf.drawCentredString(415,555,'Faixa de indicação:')
        tex = Paragraph(str(request.POST.get("resultados.valor_ref"))) # instanciando o paragrafo depois de importar a biblioteca
        tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,470,555)


        pdf.drawCentredString(396,540,'Resolução:')

        tex = Paragraph(str(request.POST.get("resolucao"))) # instanciando o paragrafo depois de importar a biblioteca
        tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,470,540)


        pdf.drawCentredString(415,525,'Faixa de Calibração:')

        tex = Paragraph(str(request.POST.get("resultados.valor_ref"))) # instanciando o paragrafo depois de importar a biblioteca
        tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,470,525)

        pdf.drawCentredString(410,510,'Ordem de Serviço:')
        
        tex = Paragraph("{}/{}".format(str(request.POST.get("ordem_servico")), ano_atual)) # instanciando o paragrafo depois de importar a biblioteca
        tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,470,510)


        pdf.drawCentredString(410,495,'Data da Calibração:')

        tex = Paragraph(str(request.POST.get("data_calibracao"))) # instanciando o paragrafo depois de importar a biblioteca
        tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,470,495)


        pdf.drawCentredString(410,480,'Data da Emissão:')

        tex = Paragraph(str(request.POST.get("data_emissao"))) # instanciando o paragrafo depois de importar a biblioteca
        tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
        tex.drawOn(pdf,460,480)

    # Function for the second part of the certificate
    def segunda_parte_pdf():
        pdf.setStrokeColor(colors.lightgrey)
        pdf.setLineWidth(18)
        pdf.line(50,465,600,465) # argumentos(y-inicial,x-inicial,y-final,x-final)
        pdf.drawCentredString(120,465,'3. Dados do Ambiente')

        pdf.drawCentredString(100,440,'Temperatura:')
        pdf.drawCentredString(190,440,request.POST.get("temperatura"))

        pdf.drawCentredString(300,440,'Pressão Barométrica:')
        pdf.drawCentredString(400,440,request.POST.get("pressao"))

        pdf.drawCentredString(500,440,'Umidade Relativa:')
        pdf.drawCentredString(580,440,request.POST.get("umidade"))

        pdf.setStrokeColor(colors.lightgrey)
        pdf.setLineWidth(18)
        pdf.line(50,400,600,400) # argumentos(y-inicial,x-inicial,y-final,x-final)
        pdf.drawCentredString(116,400,'4. Padrões Utilizados')
        pdf.drawCentredString(108,375,'Código')
        pdf.drawCentredString(108,355,str(request.POST.get("novo_padrao.serie")))
        pdf.drawCentredString(208,375,'Descrição')
        pdf.drawCentredString(208,355,str(request.POST.get("novo_padrao.observacoes")))
        pdf.drawCentredString(308,375,'Certificado')
        pdf.drawCentredString(308,355,str(request.POST.get("novo_padrao")))
        pdf.drawCentredString(408,375,'Rastreabilidade')
        pdf.drawCentredString(408,355,'Rastreabilidade')
        pdf.drawCentredString(508,375,'Validade')
        pdf.drawCentredString(508,355,str(request.POST.get("novo_padrao.prox_verificacao")))

        pdf.setStrokeColor(colors.lightgrey)
        pdf.setLineWidth(18)
        pdf.line(50,330,600,330) # argumentos(y-inicial,x-inicial,y-final,x-final)
        pdf.drawCentredString(108,330,'5. Procedimentos')
        pdf.drawCentredString(108,310,str(request.POST.get("dados_procedimento")))

        pdf.drawInlineImage(
            r'static/img/assinatura.png',
            135, 0,
            preserveAspectRatio=True
        )

     
    def terceira_parte_pdf():
        pdf.showPage()
        pdf.drawInlineImage(
            r'static/img/Imagem - de cima.jpeg',
            50, 700,
            preserveAspectRatio=True
        )
        pdf.setFontSize(15)
        pdf.setFillColor(colors.black)
        pdf.drawCentredString(480,748,'CERTIFICADO DE CALIBRAÇÃO')
        pdf.setFontSize(9)
        pdf.drawCentredString(560,734,str(request.POST.get("calibracao"))) # argumentos(y,x,calibracao) 
        
        pdf.setStrokeColor(colors.lightgrey)
        pdf.setLineWidth(18)
        pdf.line(50,700,600,700) # argumentos(y-inicial,x-inicial,y-final,x-final)
        pdf.drawCentredString(135,700,'6. Resultados da Calibração')

        dados = {'(VMA)':[0.1, 1, 2, 5, 10, 20, 50, request.POST.get("resultados.valor_ref"), 150, 220],
                '(VR) \n(g)':[0.1, 1, 2, 5, 10, 20, 50, request.POST.get("resultados.valor_ref"), 150, 220],
                '(SMC) \n(g)':[0.1, 1, 2, 5, 10, 20, 50, request.POST.get("resultados.media"), 150, 220],
                '(E) \nErro\n(g)':[0,0,0,0,0,0,0,request.POST.get("resultados.erro"),0,0],
                '(U) \nIncerteza Expandida':[0,0,0,0,0,0,0,request.POST.get("resultados.incerteza_expandida"),0,0],
                '(k) \nFator de Abrangência':[0,0,0,0,0,0,0,request.POST.get("resultados.fator_de_abrangencia9045"),0,0],
                '(veff)\nGraus de Liberdade':[0,0,0,0,0,0,0,request.POST.get("resultados.grau_de_liberdade_veff"),0,0],
                }

        df = pd.DataFrame(dados)

        matriz = [df.columns.tolist()] + df.values.tolist()

        tabela = Table(matriz)

        tabela.setStyle([
            ('GRID',(0,0),(-1,-1),1,'black'),
            ]) # estilizar a tabela 


        tabela.wrapOn(pdf,0, 0) # no caso da tabela não precisa colocar posições...
        tabela.drawOn(pdf,50,450)
        

        # Desenhar o texto centralizado com a fonte definida
        pdf.drawCentredString(245, 440, 'VMA: Valor Medido Antes do Ajuste VR: Valor de Refência SMC: Sistema de Medição à Calibrar')    
        
        pdf.drawInlineImage(
            r'static/img/assinatura.png',
            135, 0,
            preserveAspectRatio=True
        )


        

    # Call the functions with the data from the form
    primeira_parte_pdf(pdf)
    segunda_parte_pdf()
    terceira_parte_pdf()

    # Save the PDF and prepare the response
    pdf.showPage()
    pdf.drawInlineImage(
            r'static/img/Imagem - de cima.jpeg',
            50, 700,
            preserveAspectRatio=True
        )
    pdf.setFontSize(15)
    pdf.setFillColor(colors.black)
    pdf.drawCentredString(480,748,'CERTIFICADO DE CALIBRAÇÃO')
    pdf.setFontSize(9)
    pdf.drawCentredString(560,734,str(request.POST.get("calibracao"))) # argumentos(y,x,calibracao) 
    pdf.setStrokeColor(colors.lightgrey)
    pdf.setLineWidth(18)
    pdf.line(50,690,600,690) # argumentos(y-inicial,x-inicial,y-final,x-final)
    pdf.drawCentredString(135,685,'7. Excentricidade e Repetições')


    pdf.setStrokeColor(colors.lightgrey)
    pdf.setLineWidth(18)
    pdf.line(48,590,600,590) # argumentos(y-inicial,x-inicial,y-final,x-final)
    pdf.drawCentredString(100,585,'8. Observações')
    pdf.drawInlineImage(
            r'static/img/assinatura.png',
            135, 0,
            preserveAspectRatio=True
        )
    pdf.save()

    # Prepare the response with the generated PDF
    with open(pdf_file_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="calibracao_{}_{}.pdf"'.format(ano_atual, request.POST.get("customer.name"))

    return response








# processo trena
def trena_processo(request):
    customers = Customers_main.objects.values("id", "name").distinct()
    resultados = None
    customer = None
    instruments = None
    selected_instrument = None

    if request.method == "POST":
        customer_id = request.POST.get("name")
        print(customer_id)
        if customer_id is not None and int(customer_id) != 0:
            customer = Customers_main.objects.get(id=customer_id)
            instruments = InstrumentsInstruments.objects.filter(id_customer=customer_id)

        instrument_id = request.POST.get("instrumentSelect")

        if instrument_id:
            selected_instrument = InstrumentsInstruments.objects.get(id=instrument_id)

        numeros = []
        for i in range(1, 4):
            numero = request.POST.get(f"numero{i}")
            if numero:
                numeros.append(float(numero))
            else:
                numeros.append(0.0)

        if numeros:
            resultados = calcular_trena(
                numeros
            )  # Chamar função para realizar cálculos passando os inputs.

    return render(
        request,
        "calibracao/trena.html",
        {
            "resultados": resultados,
            "customers": customers,
            "customer": customer,
            "instruments": instruments,
            "selected_instrument": selected_instrument,
        },
    )
