from Token import *
from TabelaDeSimbolos import TabelaDeSimbolos


def get_tokens(conteudo):
    p = [0, -1] # Linha e Coluna
    tabela = TabelaDeSimbolos()
    lista_tokens = []
    #print("-----------------Tokens-----------------")
    
    while(True):
        tk = get_token(conteudo, tabela, p)
        lista_tokens.append(tk)
        #tk.printToken()

        if tk.nome == "EOF":
            break
    
    #print("-----------------Tabela de símbolos-----------------")
    #tabela.printarTabela()
    return lista_tokens, tabela

def getKeyWord(tabela, lexema):
    for key in tabela.linhas:
        if key.lexema == lexema:
             return key
    return None

def lookahead(p):
    p[1] -= 1

def prox(file, p):
    if p[1] + 1 >= len(file[p[0]]):
        return None
    return file[p[0]][p[1]+1]

def addCaracter(temp, char):
    if char != None:
        return temp + char
    return temp + " "

def isFunction(char, func):
    if char is not None:
        return func(char)
    return False

def get_token(file, tabela, p):
    state = 1  # estado inicial 
    temp = ""
    char = ""
    while True:
        match state:
            case 1:
                char = prox(file, p) 
                p[1] += 1
                temp = char
                if char == None:
                    return Token("EOF", None, [p[0], p[1]+2])
                elif isFunction(char, str.isalpha):
                    state = 2
                elif char == ',':
                    state = 4
                elif char == ';':
                    state = 5
                elif char == ':':
                    state = 6
                elif char == '%':
                    state = 7
                elif char == '=':
                    state = 9
                elif char == '<':
                    state = 10
                elif char == '>':
                    state = 15
                elif char == '+':
                    state = 18
                elif char == '-':
                    state = 19
                elif char == '*':
                    state = 22
                elif char == '/':
                    state = 25
                elif char == '^':
                    state = 28
                elif char == "'":
                    state = 29
                elif char in '0123456789':
                    state = 32
                elif char == '(':
                    state = 41
                elif char == ')':
                    state = 42
                elif char == ' ' or char == '\t' or char == '\n':
                    if char == '\n':
                        p[0] += 1
                        p[1] = -1
                    elif char == '\t':
                        p[1] += 3
                    state = 43
                else:
                    raise Exception("Caracter Inválido")
            case 2:
                char = prox(file, p) 
                p[1] += 1
                temp = addCaracter(temp, char)
                if isFunction(char, str.isalpha) or isFunction(char, str.isnumeric):
                    state = 2
                else:
                    state = 3
            case 3:
                lookahead(p)
                X = getKeyWord(tabela, temp[:-1])
                if X == None:
                    tabela.adiciona_token("ID", temp[:-1], None, None)
                    return Token("ID", temp[:-1], p)
                return Token(X.nome, X.lexema, p)
            case 4:
                return Token(",", None, p)
            case 5:
                return Token(";", None, p)
            case 6:
                return Token(":", None, p)
            case 7:
                char = prox(file, p)
                p[1] += 1
                if char == '%':
                    state = 8
                else:
                    state = 7 
            case 8:
                state = 1
            case 9:
                return Token("relop", "EQ", [p[0], p[1]+1])
            case 10:
                char = prox(file, p)
                p[1] += 1
                temp = addCaracter(temp, char)
                if char == '=':
                    state = 12
                elif char == '>':
                    state = 13
                elif char == '-':
                    state = 14
                else:
                    state = 11
            case 11:
                return Token("relop", "LT", p)
            case 12:
                return Token("relop", "LE", p)
            case 13:
                return Token("relop", "NE", p)
            case 14:
                return Token("<-", None, p)
            case 15:
                char = prox(file, p)
                p[1] += 1
                temp = addCaracter(temp, char)
                if char == '=':
                    state = 16
                else:
                    state = 17
            case 16:
                return Token("relop", "GE", p)
            case 17:
                lookahead(p)
                return Token("relop", "GT", p)
            case 18:
                 return Token("+", None, p)
            case 19:
                char = prox(file, p)
                p[1] += 1
                temp = addCaracter(temp, char)
                if char == ">":
                    state = 20
                else:
                    state = 21
            case 20:
                return Token("->", None, p)
            case 21:
                lookahead(p)
                return Token("-", None, p)
            case 22:
                char = prox(file, p)
                p[1] += 1
                temp = addCaracter(temp, char)
                if char == '/':
                    state = 23
                else:
                    state = 24
            case 23:
                return Token("*/", None, p)
            case 24:
                if char != None: lookahead(p)
                return Token("*", None, p)
            case 25:
                char = prox(file, p) 
                p[1] += 1
                temp = addCaracter(temp, char)
                if char == "*":
                    state = 26
                else:
                    state = 27
            case 26:
                return Token("/*", None, p)
            case 27:
                if char != None: lookahead(p)
                return Token("/", None, p)
            case 28:
                return Token("^", None, p)
            case 29:
                char = prox(file, p) 
                p[1] += 1
                temp = addCaracter(temp, char)
                if char != "'":
                    state = 30
                else:
                    raise Exception("Esperado valor diferente de '")
            case 30:
                char = prox(file, p)
                p[1] += 1
                temp = addCaracter(temp, char)
                if char == "'":
                    state = 31
                else:
                    raise Exception("Esperado '")
            case 31:
                tabela.adiciona_token("CONST_CHAR", temp, temp, "char")
                return Token("CONST_CHAR", temp, p)
            case 32:
                char = prox(file, p)
                p[1] += 1
                temp = addCaracter(temp, char)
                if isFunction(char, str.isnumeric):
                    state = 32
                elif char == '.':
                    state = 34
                elif char == 'E':
                    state = 37
                else:
                    state = 33
            case 33:
                lookahead(p)
                tabela.adiciona_token("CONST_NUM", temp[:-1], int(temp[:-1]), "int")
                return Token("CONST_NUM", temp[:-1], p)
            case 34:
                char = prox(file, p)
                p[1] += 1
                temp = addCaracter(temp, char)
                if isFunction(char, str.isnumeric):
                    state = 35
                else:
                    raise Exception("Esperado um digito")
            case 35:
                char = prox(file, p)
                p[1] += 1
                temp = addCaracter(temp, char)
                if isFunction(char, str.isnumeric):
                    state = 35
                elif char == 'E':
                    state = 37
                else:
                    state = 36
            case 36:
                lookahead(p)
                tabela.adiciona_token("CONST_NUM", temp[:-1], float(temp[:-1]), "float")
                return Token("CONST_NUM", temp[:-1], p)
            case 37:
                char = prox(file, p)
                p[1] += 1
                temp = addCaracter(temp, char)
                if char in '+-':
                    state = 38
                elif isFunction(char, str.isnumeric):
                    state = 39
                else:
                    raise Exception("Esperado um digito")
            case 38:
                char = prox(file, p)
                p[1] += 1
                temp = addCaracter(temp, char)
                if isFunction(char, str.isnumeric):
                    state = 39
                else:
                    raise Exception("Esperado um digito")
            case 39:
                char = prox(file, p)
                p[1] += 1
                temp = addCaracter(temp, char)
                if isFunction(char, str.isnumeric):
                    state = 39
                else:
                    state = 40
            case 40:
                lookahead(p)
                tabela.adiciona_token("CONST_NUM", temp[:-1], float(temp[:-1]), "float")
                return Token("CONST_NUM", temp[:-1], p)
            case 41:
                return Token("(", None, p)
            case 42:
                return Token(")", None, p)
            case 43:
                char = prox(file, p)
                temp = addCaracter(temp, char)
                if char == " " or char == '\t' or char == '\n':
                    if char == '\n':
                        p[0] += 1
                        p[1] = -1
                    elif char == ' ':
                        p[1] += 1
                    elif char == '\t':
                        p[1] += 4
                    state = 43
                else:
                    state = 44
            case 44:
                lookahead(p)
                p[1] += 1
                state = 1 
            case _:
                raise Exception("Estado "+ str(state)+ " inválido")