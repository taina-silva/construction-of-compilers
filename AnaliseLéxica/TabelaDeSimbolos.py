class LinhaTabelaSimbolos(object):
    def __init__(self, nome, lexema, valor, tipo_dado):
        self.nome = nome
        self.lexema = lexema 
        self.valor = valor 
        self.tipo_dado = tipo_dado

    def printarLinha(self):
        print (f"{self.nome}, {self.lexema}, {self.valor}, {self.tipo_dado}")

class TabelaDeSimbolos(object):
    def __init__(self):
        self.linhas = [
            LinhaTabelaSimbolos("programa", "programa", None, None),
            LinhaTabelaSimbolos("se", "se", None, None),
            LinhaTabelaSimbolos("entao", "entao", None, None),
            LinhaTabelaSimbolos("senao", "senao", None, None),
            LinhaTabelaSimbolos("enquanto", "enquanto", None, None),
            LinhaTabelaSimbolos("faca", "faca", None, None),
            LinhaTabelaSimbolos("repita", "repita", None, None),
            LinhaTabelaSimbolos("ate", "ate", None, None),
            LinhaTabelaSimbolos("int", "int", None, None),
            LinhaTabelaSimbolos("char", "char", None, None),
            LinhaTabelaSimbolos("float", "float", None, None),
        ]
    
    def adiciona_linha(self, linha_tabela_simbolos):
        self.linhas.append(linha_tabela_simbolos)

    def adiciona_token(self, nome, lexema, valor, tipo):
        # Cria uma nova linha com o token fornecido
        nova_linha = LinhaTabelaSimbolos(nome, lexema, valor, tipo)
        
        # Verifica se o token e seu atributo não estão presentes em nenhuma linha existente
        if not any(nova_linha.nome == linha.nome and nova_linha.lexema == linha.lexema for linha in self.linhas):
            # Adiciona a nova linha à tabela de símbolos
            self.linhas.append(nova_linha)

    def prox_linha(self):
        return len(self.linhas)
    
    def printarTabela(self):
        for linha in self.linhas:
            linha.printarLinha()