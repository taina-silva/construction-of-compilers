from treelib import Node, Tree
from AnaliseSintática.TabelaPreditiva import *

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
            tag_atual = Tag(producao.tag, producao.eh_terminal)
            # Criação nó da árvore
            node = Node()

            # Identificador do nó
            tag_atual.identificador = node.identifier
            node.data = tag_atual

            # Adiciona nó no pai X
            arvore.add_node(node, parent=X.identificador)  
            # Adiciona na pilha          
            P.append(tag_atual)


def get_nodes(lista_tokens, lista_producoes, nome_tag):
    arvore = Tree()
    tag_inicial = Tag(nome_tag, False)
    node = Node()
    tag_inicial.identificador = node.identifier
    node.data = tag_inicial
    arvore.add_node(node)
    tabelas = Tabelas(lista_producoes)

    pos_token = 0
    P = [] # Pilha
    P.append(tag_inicial)    

    while(len(P) > 0):
        
        X = P[-1] # Topo(P)
        token_atual = lista_tokens[pos_token]
        nome_token = token_atual.nome

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
    
    with open("arvore.txt", "w"):
        pass

    arvore.save2file("arvore.txt",data_property='tag')
    return arvore
            

