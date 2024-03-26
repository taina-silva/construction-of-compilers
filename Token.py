class Token(object):

    def __init__(self, nome, atributo, posicoes):
        self.nome = nome
        self.atributo = atributo
        self.linha = posicoes[0] # Linha
        if atributo == None:
            #print(posicoes[1], " ", len(nome))
            self.coluna = posicoes[1]-len(nome) # Coluna
        else:
            self.coluna = posicoes[1]-len(atributo) # Coluna

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