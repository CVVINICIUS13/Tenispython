import csv
from tenis import Tenis

def escreveArquivo(nome, quantidade, preco,cor,marca,qualidade):
    with open('pruduto.csv', 'a', newline='') as csvfile:
        escreve_produto = csv.writer(csvfile, delimiter=',')
        escreve_produto.writerow([nome, preco, cor, marca, quantidade,qualidade])
        print("### PRODUTO ",nome, "adicionado com sucesso! ###")

produtos = []
print("### BEM VINDO A TELA DE CADASTRO DE PRODUTOS ###")
while(True):
    print("\nNOVO PRODUTO:")
    nome = input("Digite o nome: \n")
    marca = input("Digite a marca: \n")
    cor = input("Digite o nome da cor: \n")
    preco = 10000000
    quantidade = 1
    qualidade = input("Digite a qualidade: \n")
    novoProduto = Tenis(nome, quantidade, preco,cor,marca,qualidade)
    
    escreveArquivo(nome, quantidade, preco,cor , marca, qualidade)
    produtos.append(novoProduto)