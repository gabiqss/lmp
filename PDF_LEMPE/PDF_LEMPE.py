from reportlab.pdfgen import canvas
from reportlab.lib import colors
import variaveis as var
from reportlab.platypus import Paragraph
from reportlab.platypus import Table
import pandas as pd 

# FUNÇÃO DE VERIFICAÇÃO DE LINHAS NO PDF: 
def drawMyRuler(pdf):
    pdf.drawString(100,810, 'x100')
    pdf.drawString(200,810, 'x200')
    pdf.drawString(300,810, 'x300')
    pdf.drawString(400,810, 'x400')
    pdf.drawString(500,810, 'x500')
    
    pdf.drawString(10,10, 'y,10')
    pdf.drawString(10,100, 'y,100')
    pdf.drawString(10,200, 'y,200')
    pdf.drawString(10,300, 'y,300')
    pdf.drawString(10,400, 'y,400')
    pdf.drawString(10,500, 'y,500')
    pdf.drawString(10,600, 'y,600')
    pdf.drawString(10,700, 'y,700')
    pdf.drawString(10,800, 'y,800')

pdf = canvas.Canvas('Certificado.pdf')

# FUNÇÃO DA PRIMEIRA PARTE DO CERTIFICIADO

# colocando a imagem de cima: 

def primeira_parte_pdf(calibracao,cliente,endereco,solicitante,instrumento,identificacao,numero_deserie,modelo,fabricante,Classe,e,localizacao,faixa_indicacao,resolucao,faixa_de_calibracao,ordem_de_servico,data_da_calibracao,data_da_emissao):
    
    pdf.drawInlineImage(
        r'C:\Users\jonat\Desktop\PROJETOS\PDF_LEMPE\Imagem - de cima.jpeg',
        50,750,
        preserveAspectRatio=True
    )

    # posicionando o inicio do pdf 

    pdf.setFontSize(15)
    pdf.setFillColor(colors.black)
    pdf.drawCentredString(480,748,'CERTIFICADO DE CALIBRAÇÃO')
    pdf.setFontSize(9)
    pdf.drawCentredString(560,734,calibracao) 

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
    texto = Paragraph(cliente) # instanciando o paragrafo depois de importar a biblioteca
    texto.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
    texto.drawOn(pdf,125,666 ) # colocando o paragrafo no pdf.....


    pdf.drawCentredString(90,650,'Endereço:')

    texto = Paragraph(endereco) # instanciando o paragrafo depois de importar a biblioteca
    texto.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
    texto.drawOn(pdf,125,646 ) # colocando o paragrafo no pdf.....

    pdf.drawCentredString(90,630,'Solicitante:')

    texto = Paragraph(solicitante) # instanciando o paragrafo depois de importar a biblioteca
    texto.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
    texto.drawOn(pdf,125,628 ) # colocando o paragrafo no pdf.....


    # 2 - DADOS DO INSTRUMENTO: 

    pdf.setStrokeColor(colors.lightgrey)
    pdf.setLineWidth(18)
    pdf.line(48,590,600,590) # argumentos(y-inicial,x-inicial,y-final,x-final)
    pdf.drawCentredString(146,585,'2. Dados do Instrumento Calibrado')

    pdf.drawCentredString(104,570,' Instrumento:     ')

    tex = Paragraph(instrumento) # instanciando o paragrafo depois de importar a biblioteca
    tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,150,567 )

    pdf.drawCentredString(104,555,' Identificação:   ')

    tex = Paragraph(identificacao) # instanciando o paragrafo depois de importar a biblioteca
    tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,150,553 )


    pdf.drawCentredString(108,540,'  Número de Série: ')

    tex = Paragraph(numero_deserie) # instanciando o paragrafo depois de importar a biblioteca
    tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,150,539)


    pdf.drawCentredString(100,525,' Modelo:          ')

    tex = Paragraph(modelo) # instanciando o paragrafo depois de importar a biblioteca
    tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,150,525)


    pdf.drawCentredString(100,510,'  Fabricante:      ')

    tex = Paragraph(fabricante) # instanciando o paragrafo depois de importar a biblioteca
    tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,150,510)

    pdf.drawCentredString(100,495,' Classe:          ')

    tex = Paragraph(Classe) # instanciando o paragrafo depois de importar a biblioteca
    tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,150,490)

    pdf.drawCentredString(100,480,'e:               ')

    tex = Paragraph(e) # instanciando o paragrafo depois de importar a biblioteca
    tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,150,480)

    pdf.drawCentredString(400,570,'Localização:')

    tex = Paragraph(localizacao) # instanciando o paragrafo depois de importar a biblioteca
    tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,470,570)


    pdf.drawCentredString(415,555,'Faixa de indicação:')

    tex = Paragraph(faixa_indicacao) # instanciando o paragrafo depois de importar a biblioteca
    tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,470,555)


    pdf.drawCentredString(396,540,'Resolução:')

    tex = Paragraph(resolucao) # instanciando o paragrafo depois de importar a biblioteca
    tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,470,540)


    pdf.drawCentredString(415,525,'Faixa de Calibração:')

    tex = Paragraph(faixa_de_calibracao) # instanciando o paragrafo depois de importar a biblioteca
    tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,470,525)

    pdf.drawCentredString(410,510,'Ordem de Serviço:')

    tex = Paragraph(ordem_de_servico) # instanciando o paragrafo depois de importar a biblioteca
    tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,470,510)


    pdf.drawCentredString(410,495,'Data da Calibração:')

    tex = Paragraph(data_da_calibracao) # instanciando o paragrafo depois de importar a biblioteca
    tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,470,495)


    pdf.drawCentredString(410,480,'Data da Emissão:')

    tex = Paragraph(data_da_emissao) # instanciando o paragrafo depois de importar a biblioteca
    tex.wrapOn(pdf,400,100) # definindo o tamanho do paragrafo 
    tex.drawOn(pdf,470,480)

primeira_parte_pdf(var.c_calibração,var.cliente,var.endereco,var.solicitante,
                   var.instrumento,var.identificacao,var.numero_serie,
                   var.modelo,var.fabricante,var.Classe,
                   var.e,var.localizacao,var.faixa_de_indicacao,
                   var.resolucao,var.faixa_de_calibracao,var.ordem_de_servico,var.data_da_calibracao,
                   var.data_da_emissão)

# 3 - Dados do Ambiente:

def segunda_parte_pdf(Temperatura,pressao_barometrica,umidade_relativa):
    pdf.setStrokeColor(colors.lightgrey)
    pdf.setLineWidth(18)
    pdf.line(50,465,600,465) # argumentos(y-inicial,x-inicial,y-final,x-final)
    pdf.drawCentredString(120,465,'3. Dados do Ambiente')

    pdf.drawCentredString(100,440,'Temperatura:')
    pdf.drawCentredString(190,440,Temperatura) 

    pdf.drawCentredString(300,440,'Pressão Barométrica:')
    pdf.drawCentredString(400,440,pressao_barometrica)

    pdf.drawCentredString(500,440,'Umidade Relativa:')
    pdf.drawCentredString(580,440,umidade_relativa)

    pdf.setStrokeColor(colors.lightgrey)
    pdf.setLineWidth(18)
    pdf.line(50,400,600,400) # argumentos(y-inicial,x-inicial,y-final,x-final)
    pdf.drawCentredString(116,400,'4. Padrões Utilizados')


    pdf.setStrokeColor(colors.lightgrey)
    pdf.setLineWidth(18)
    pdf.line(50,300,600,300) # argumentos(y-inicial,x-inicial,y-final,x-final)
    pdf.drawCentredString(108,300,'5. Procedimentos')

segunda_parte_pdf(var.temperatura,var.pressao_barometrica,var.umidade_relativa)

# 6 - Resultados da Calibração: 
def terceira_parte_pdf():
    
    pdf.setStrokeColor(colors.lightgrey)
    pdf.setLineWidth(18)
    pdf.line(50,250,600,250) # argumentos(y-inicial,x-inicial,y-final,x-final)
    pdf.drawCentredString(135,250,'6. Resultados da Calibração')

    dados = {'(VMA)':[0,1001,1.0001,2.0003,5.0003,10.0002,20.0002,50.0000,100.0003,150.0007,220.0003],
            '(VR (g))':[0,1001,1.0001,2.0003,5.0003,10.0002,20.0002,50.0000,100.0003,150.0007,220.0003],
            '(SMC(g))':[0,1001,1.0001,2.0003,5.0003,10.0002,20.0002,50.0000,100.0003,150.0007,220.0003],
            '((E) erro)':[0,1001,1.0001,2.0003,5.0003,10.0002,20.0002,50.0000,100.0003,150.0007,220.0003],
            '((U) incerteza Ex)':[0,1001,1.0001,2.0003,5.0003,10.0002,20.0002,50.0000,100.0003,150.0007,220.0003],
            '((k) Fator de Abrang)':[0,1001,1.0001,2.0003,5.0003,10.0002,20.0002,50.0000,100.0003,150.0007,220.0003],
            '((veff)Graus de Lib)':[0,1001,1.0001,2.0003,5.0003,10.0002,20.0002,50.0000,100.0003,150.0007,220.0003],
            }

    df = pd.DataFrame(dados)

    matriz = [df.columns.tolist()] + df.values.tolist()

    tabela = Table(matriz)

    tabela.setStyle([
        ('GRID',(0,0),(-1,-1),1,'black'),
        ]) # estilizar a tabela 


    tabela.wrapOn(pdf,0, 0) # no caso da tabela não precisa colocar posições...
    tabela.drawOn(pdf,50,2)



    drawMyRuler(pdf)

terceira_parte_pdf()

#adicionando nova pagina: 

pdf.showPage()

pdf.setStrokeColor(colors.lightgrey)
pdf.setLineWidth(18)
pdf.line(50,690,600,690) # argumentos(y-inicial,x-inicial,y-final,x-final)
pdf.drawCentredString(115,685,'7. Excentricidade e Repetições')


pdf.setStrokeColor(colors.lightgrey)
pdf.setLineWidth(18)
pdf.line(48,590,600,590) # argumentos(y-inicial,x-inicial,y-final,x-final)
pdf.drawCentredString(146,585,'8. Observações')

drawMyRuler(pdf)

pdf.save()