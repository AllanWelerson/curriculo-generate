import Curriculo
from fpdf import FPDF

def gerarPDF(pdf, dados):

    pdf.cell(0, 5, dados["nome"], 0, 1, 'C')
    pdf.set_font('Arial', '', 12)
    pdf = dadosPessoais(pdf, dados)
    pdf = formacao(pdf, dados)



    return pdf


def dadosPessoais(pdf, dados):

    nacionalidade_idade = dados["nacionalidade"] + ', ' + dados["idade"] + ' Anos'
    pdf.cell(0, 10, nacionalidade_idade, 0, 1, 'C')
    pdf.cell(0, 10, dados["email"], 0, 1, 'C')
    telefone1 = 'Telefones: ' + dados['telefone1']
    telefone2 = dados['telefone2']
    telefone3 = dados['telefone3']


    if len(telefone2) > 0:
        telefone1 += ' / ' + telefone2

    if len(telefone3) > 0:
        telefone1 += ' / ' + telefone3

    pdf.cell(0, 10, telefone1, 0, 1, 'C')

    pdf.cell(0, 10, dados["endereco"], 0, 1, 'C')

    cidade_estado_cep =   dados["bairro"] + ' - ' + dados["cidade"] + ' - ' + dados["estado"] + ' - ' + dados["cep"]
    pdf.cell(0, 10, cidade_estado_cep, 0, 1, 'C')

    return pdf

def formacao(pdf, dados):


    pdf.cell(0, 10, "Formação academica", 1, 1, 'C')
    pdf.cell(0, 10, "", 0, 1, 'L')



    pdf = addNovaFormacao(pdf,  dados['curso1_desc'], dados['curso1_instituicao'], dados['curso1_nivel'],
                                dados['curso1_situacao'], dados['curso1_periodo'], dados['curso1_horario']
                          )

    pdf = addNovaFormacao(pdf, dados['curso2_desc'], dados['curso2_instituicao'], dados['curso2_nivel'],
                          dados['curso2_situacao'], dados['curso2_periodo'], dados['curso2_horario']
                          )
    pdf = mostraGrau(pdf, dados)




    return pdf

def addNovaFormacao(pdf, desc, instituicao, nivel, situacao, periodo, turno):

    if len(desc) > 0 and len(instituicao) > 0:
        txt1 = ' - ' + nivel + ' em ' + desc + ' - ' + instituicao
        if situacao == 'concluido':
            periodo = ''
            turno = ''
        else:
            periodo =  ' -' + periodo + ' Periodo '
            turno = ' - ' + turno
        txt2 =  situacao + periodo + turno
        pdf.cell(0, 10, txt1, 0, 1, 'L')
        pdf.cell(0, 10, "  " +txt2, 0, 1, 'L')


    return pdf

def mostraGrau(pdf, dados):

    curso1_desc = dados['curso1_desc']
    curso1_instituicao = dados['curso1_instituicao']
    curso2_desc = dados['curso2_desc']
    curso2_instituicao = dados['curso2_instituicao']

    if len(curso1_desc) == 0 :
        pdf.cell(0, 10, dados['grau'] , 0, 1, 'L')

    return pdf