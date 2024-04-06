from treelib import Node, Tree
from AnaliseSintática.TabelaPreditiva import *

def downloadTree(tree):
    for node in tree.all_nodes():
        print(node.data)
        node.data = node.data.tag
    tree.save2file("arvore.txt")


def printar_tags(P):
    print("################")
    for producao in P:
        print(producao.tag)
    print("################")

def trata_producao(arvore, tabelas, P, X, nome_token):
    nome_producao = tabelas.tabela_preventivas[X.tag][nome_token]
    lista_producoes = tabelas.tabela_producoes[nome_producao]

    for producao in reversed(lista_producoes):
        if producao.tag != "<vazio>":
            #node = Node(data=producao)
            #producao.identificador = node.identifier
            #arvore.add_node(node, parent=X.identificador)
            #downloadTree(arvore)
            
            P.append(producao)
    print("\n---------------------\n")

def get_nodes(lista_tokens, tabela_simbolos, lista_producoes, nome_tag):
    arvore = Tree()
    tag_inicial = Tag(nome_tag, False)
    node = arvore.create_node(data=tag_inicial)
    tag_inicial.identificador = node.identifier
    tabelas = Tabelas(lista_producoes)

    pos_token = 0
    P = [] # Pilha
    P.append(tag_inicial)    

    while(len(P) > 0):
        # printar_tags(P)
        
        X = P[-1] # Topo(P)
        token_atual = lista_tokens[pos_token]
        nome_token = token_atual.nome

        print("\n")
        print(nome_token)
        print(X.tag)
        print("\n")

        if X.eh_terminal:
            if X.tag == nome_token:
                P.pop()
                pos_token += 1 # Próximo Token
            else:
                print("\n")
                print(nome_token)
                print(X.tag)
                print("\n")

                raise Exception("Não existe essa produção!")
        else:
            if nome_token not in tabelas.tabela_preventivas[X.tag]:
                print("\n")
                print(nome_token)
                print(X.tag)
                print("\n")

                raise Exception("Não existe essa produção!")   
            else:
                P.pop()
                trata_producao(arvore, tabelas, P, X, nome_token)

                
    if pos_token+1 != len(lista_tokens):
        raise Exception("Nao foi verificado todos os tokens")
    
    arvore.save2file("arvore.txt")
    return arvore
            

