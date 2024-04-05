from AnalisadorSintático import *
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
d_folder_path = os.path.join(current_dir, '..', 'AnaliseLéxica')
sys.path.append(d_folder_path)

from AnalisadorLexico import *
from main1 import *

def ListPro(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        producoes = file.read().split("\n")

    for i in range(len(producoes)):
        producoes[i] = producoes[i].split(' ')

    name = 'P'
    lista_producoes = []

    for i in range(len(producoes)):
        aux = []
        for item in producoes[i]:
            if item[0] == "<" and item[-1] == ">":
                aux.append([item, False])
            else:
                aux.append([item, True])

        lista_producoes.append([name + str(i+1), aux])

    return lista_producoes

if __name__ == "__main__":
    nome_tag = "<inicio>"

    lista_tokens, tabela_simbolos = get_tokens(read("../teste.txt"))
    
    lista_producoes = ListPro("producoes.txt")
    
    get_nodes(lista_tokens, tabela_simbolos, lista_producoes, nome_tag)