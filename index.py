from flask import Flask, render_template, request, make_response
from fpdf import FPDF
from CurriculoPDF import gerarPDF, dadosPessoais
import Curriculo

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/gerar", methods=["POST"])
def gerarPdf():
    dados = Curriculo.dadosCurriculo(request)
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('Arial', 'B', 14)
    pdf = gerarPDF(pdf, dados)
    response = make_response(pdf.output(dest='S').encode('latin-1'))
    response.headers.set('Content-Disposition', 'attachment', filename='curriculo' + '.pdf')
    response.headers.set('Content-Type', 'application/pdf')
    return response


