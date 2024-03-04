from Token import Token  # Certifique-se de importar o módulo Token, se necessário

class LinhaTabelaSimbolos(object):
    def __init__(self, token, lexema, valor, tipo_dado):
        self.token = token
        self.lexema = lexema 
        self.valor = valor 
        self.tipo_dado = tipo_dado

    def printarLinha(self):
        print (f"{self.token}, {self.lexema}, {self.valor}, {self.tipo_dado}")

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
            LinhaTabelaSimbolos("+", "+", None, None),
            LinhaTabelaSimbolos("-", "-", None, None),
            LinhaTabelaSimbolos("*", "*", None, None),
            LinhaTabelaSimbolos("/", "/", None, None),
            LinhaTabelaSimbolos("/*", "*/", None, None),
            LinhaTabelaSimbolos("<--", "<--", None, None),
            LinhaTabelaSimbolos("^", "^", None, None),
            LinhaTabelaSimbolos(",", ",", None, None),
            LinhaTabelaSimbolos(";", ";", None, None),
            LinhaTabelaSimbolos(":", ":", None, None)
        ]
    
    def adiciona_linha(self, linha_tabela_simbolos):
        self.linhas.append(linha_tabela_simbolos)

    def adiciona_token(self, token):
        if token not in [linha.token for linha in self.linhas]:
            nova_linha = LinhaTabelaSimbolos(token, None, None, None)
            self.linhas.append(nova_linha)

    def prox_linha(self):
        return len(self.linhas)