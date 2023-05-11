from barcode import EAN13
from barcode.writer import ImageWriter
from random import choice
import string
import csv
 
header = ['Produto', 'Código', 'Quantidade', 'Preço (R$)']

while True:
    produto = str(input("Qual o produto>"))
    quantidade = int(input("Quantos produtos>"))
    preco = int(input("Qual valor>"))

    gencode = int(12)
    caracteres = string.digits 
    code = ''
    for i in range(gencode):
        code += choice(caracteres)


    barcode = EAN13(code, writer=ImageWriter())
    barcode.save(f"codigo_barras_{produto}")

    row = [produto, code, quantidade, preco]

    with open('csv_file.csv', 'w', encoding='UTF8') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(header)
        writer.writerow(row)

