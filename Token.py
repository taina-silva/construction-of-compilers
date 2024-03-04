class Token(object):

    def __init__(self, nome, atributo, linha, coluna_inicial):
        self.nome = nome
        self.atributo = atributo
        self.linha = linha
        self.coluna = abs(coluna_inicial) 

    def printToken(self):
        if self.atributo == None:
            print (" < "  + self.nome + " , null > < linha: " ,self.linha, ", coluna:", self.coluna, " >")
        else:
            print (" < "  + self.nome + " , " + self.atributo + " > < linha:" ,self.linha, ", coluna:", self.coluna, " >")
    
    def printTokens(tokens):
        for token in tokens:
            token.printToken()
    
    # def __eq__(self, other):
    #     return self.nome == other.nome and self.atributo == other.atributo