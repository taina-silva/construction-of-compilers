from Token import *
from TabelaDeSimbolos import TabelaDeSimbolos


def get_tokens(nome_arquivo):
    l = 0
    c = 0
    tabela = TabelaDeSimbolos()
    with open(nome_arquivo, 'r') as file:
        while(True):
            tk = get_token(file, tabela, l, c)
            tk.printToken()
            l = tk.linha
            c = tk.coluna
            if tk.nome == "EOF":
                break

def getKeyWord(tabela, lexema):
    for key in tabela.linhas:
        if key.lexema == lexema:
             return key
    return None

def lookahead(file):
    current_position = file.tell() 
    file.seek(current_position - 1) 


def prox(file):
    char = file.read(1)
    if not char:
        return None
    return char

def get_token(file, tabela, l, c):
    state = 1  # estado inicial 
    temp = ""
    
    while True:
        #print("Estado:", state)
        match state:
            case 1:
                char = prox(file) 
                c += 1
                if char == None:
                    return Token("EOF", None, l, c)
                temp = char
                if char.isalpha():
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
                elif char != None and char in '0123456789':
                    state = 32
                elif char == '(':
                    state = 41
                elif char == ')':
                    state = 42
                elif char == ' ' or char == '\t' or char == '\n':
                    if char == '\n':
                        l+=1
                        c = 0
                    elif char == ' ':
                        c+=1
                    elif char == '\t':
                        c+=4
                    state = 43
                else:
                    raise Exception("Caracter Inválido")
            case 2:
                char = prox(file) 
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char.isalpha() or (char != None and char in '0123456789'):
                    state = 2
                else:
                    state = 3
            case 3:
                if char != None: lookahead(file)
                c -= 1
                X = getKeyWord(tabela, temp[:-1])
                if X == None:
                    return Token("ID", temp[:-1], l, c)
                return Token(X.token, X.lexema, l, c)
            case 4:
                return Token(";", None, l, c)
            case 5:
                return Token(",", None, l, c)
            case 6:
                return Token(":", None, l, c)
            case 7:
                char = prox(file)
                c += 1
                if char == '%':
                    state = 8
                else:
                    state = 7 
            case 8:
                state = 1
            case 9:
                return Token("relop", "EQ", l, c)
            case 10:
                char = prox(file)
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char == '=':
                    state = 12
                elif char == '>':
                    state = 13
                elif char == '-':
                    state = 14
                else:
                    state = 11
            case 11:
                return Token("relop", "LT", l, c)
            case 12:
                return Token("relop", "LE", l, c)
            case 13:
                return Token("relop", "NE", l, c)
            case 14:
                return Token("<-", None, l, c)
            case 15:
                char = prox(file)
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char == '=':
                    state = 16
                else:
                    state = 17
            case 16:
                return Token("relop", "GE", l, c)
            case 17:
                if char != None: lookahead(file)
                c -= 1
                return Token("relop", "GT", l, c)
            case 18:
                 return Token("+", None, l, c)
            case 19:
                char = prox(file)
                c += 1
                if char != None: temp+=char
                else: temp +=" "
                if char == ">":
                    state = 20
                else:
                    state = 21
            case 20:
                return Token("->", None, l, c)
            case 21:
                if char != None: lookahead(file)
                c -= 1
                return Token("-", None, l, c)
            case 22:
                char = prox(file)
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char == '/':
                    state = 23
                else:
                    state = 24
            case 23:
                return Token("*/", None, l, c)
            case 24:
                if char != None: lookahead(file)
                c -= 1
                return Token("*", None, l, c)
            case 25:
                char = prox(file)
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char == '*':
                    state = 26
                else:
                    state = 27
            case 25:
                char = prox(file) 
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char == "*":
                    state = 26
                else:
                    state = 27
            case 26:
                return Token("/*", None, l, c)
            case 27:
                if char != None: lookahead(file)
                c -= 1
                return Token("/", None, l, c)
            case 28:
                return Token("^", None, l, c)
            case 29:
                char = prox(file) 
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char != "'":
                    state = 30
                else:
                    raise Exception()
            case 30:
                char = prox(file)
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char == "'":
                    state = 31
                else:
                    raise Exception()
            case 31:
                return Token("CONST_CHAR", temp, l, c)
            case 32:
                char = prox(file)
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char != None and char in '0123456789':
                    state = 33
                elif char == '.':
                        state = 34
                elif char == 'E':
                    state = 37
                else:
                    state = 33
            case 33:
                if char != None: lookahead(file)
                c -= 1
                return Token("CONST_INT", temp[:-1], l, c)
            case 34:
                char = prox(file)
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char != None and char in '0123456789':
                    state = 35
                else:
                    raise Exception()
            case 35:
                char = prox(file)
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char != None and char in '0123456789':
                    state = 35
                elif char == 'E':
                    state = 37
                else:
                    state = 36
            case 36:
                if char != None: lookahead(file)
                c -= 1
                return Token("CONST_FRAC", temp[:-1], l, c)
            case 37:
                char = prox(file)
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char == '+-':
                    state = 38
                elif char != None and char in '0123456789':
                    state = 39
                else:
                    raise Exception()
            case 38:
                char = prox(file)
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char != None and char in '0123456789':
                    state = 39
                else:
                    raise Exception()
            case 39:
                char = prox(file)
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char != None and char in '0123456789':
                    state = 39
                else:
                    state = 40
            case 40:
                if char != None: lookahead(file)
                c -= 1
                return Token("CONST_EXP", temp[:-1], l, c)
            case 41:
                return Token("(", None, l, c)
            case 42:
                return Token(")", None, l, c)
            case 43:
                char = prox(file)
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char == " " or char == '\t' or char == '\n':
                    if char == '\n':
                        l+=1
                        c = 0
                    elif char == ' ':
                        c+=1
                    elif char == '\t':
                        c+=4
                    state = 43
                else:
                    state = 44
            case 44:
                if char != None: lookahead(file)
                c -= 1
                state = 1 
            case _:
                break; #erro
