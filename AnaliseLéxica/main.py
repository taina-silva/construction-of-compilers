from AnaliseLéxica.AnalisadorLexico import *

def list_to_matrix(conteudo):
    matriz = []
    linha_atual = []

    for caractere in conteudo:
        linha_atual.append(caractere)
        if caractere == '\n':
            matriz.append(linha_atual)
            linha_atual = []  

    if linha_atual:
        matriz.append(linha_atual)

    return matriz

def read(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        conteudo = list(file.read())
    conteudo = list_to_matrix(conteudo)
    
    return conteudo

if __name__ == "__main__":
    get_tokens(read("teste.txt"))
