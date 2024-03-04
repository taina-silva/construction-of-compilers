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
                elif char == ';':
                    state = 4
                elif char == ',':
                    state = 5
                elif char == ':':
                    state = 6
                elif char == '%':
                    state = 7
                elif char == '=':
                    state = 9
                elif char == '<':
                    state = 11
                elif char == '>':
                    state = 16
                elif char == '+':
                    state = 19
                elif char == '-':
                    state = 20
                elif char == '*':
                    state = 21
                elif char == '/':
                    state = 24
                elif char == '^':
                    state = 27
                elif char == "'":
                    state = 28
                elif char != None and char in '0123456789':
                    state = 31
                elif char == '(':
                    state = 40
                elif char == ')':
                    state = 41
                elif char == ' ' or char == '\t' or char == '\n':
                    if char == '\n':
                        l+=1
                        c = 0
                    elif char == ' ':
                        c+=1
                    elif char == '\t':
                        c+=4
                    state = 42
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
                char = prox(file)
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char == '=':
                    state = 10
                else:
                    raise Exception()
            case 10:
                return Token("relop", "EQ", l, c)
            case 11:
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
                    state = 21
            case 12:
                return Token("relop", "LE", l, c)
            case 13:
                return Token("relop", "NE", l, c)
            case 14:
                char = prox(file)
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char == '-':
                    state = 15
                else:
                    raise Exception()
            case 15:
                return Token("<--", None, l, c)
            case 16:
                char = prox(file)
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char == '=':
                    state = 17
                else:
                    state = 18
            case 17:
                return Token("relop", "GE", l, c)
            case 18:
                if char != None: lookahead(file)
                c -= 1
                return Token("relop", "GT", l, c)
            case 19:
                return Token("+", None, l, c)
            case 20:
                return Token("-", None, l, c)
            case 21:
                char = prox(file)
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char == '/':
                    state = 22
                else:
                    state = 23
            case 22:
                return Token("*/", None, l, c)
            case 23:
                if char != None: lookahead(file)
                c -= 1
                return Token("*", None, l, c)
            case 24:
                char = prox(file)
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char == '*':
                    state = 25
                else:
                    state = 26
            case 25:
                return Token("/*", None, l, c)
            case 26:
                if char != None: lookahead(file)
                c -= 1
                return Token("/", None, l, c)
            case 27:
                return Token("^", None, l, c)
            case 28:
                char = prox(file) 
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char != "'":
                    state = 29
                else:
                    raise Exception()
            case 29:
                char = prox(file)
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char == "'":
                    state = 30
                else:
                    raise Exception()
            case 30:
                return Token("CONST_CHAR", temp, l, c)
            case 31:
                char = prox(file)
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char != None and char in '0123456789':
                    state = 31
                elif char == '.':
                        state = 33
                elif char == 'E':
                    state = 36
                else:
                        state = 32
            case 32:
                if char != None: lookahead(file)
                c -= 1
                return Token("CONST_INT", temp[:-1], l, c)
            case 33:
                char = prox(file)
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char != None and char in '0123456789':
                    state = 34
                else:
                    raise Exception()
            case 34:
                char = prox(file)
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char != None and char in '0123456789':
                    state = 34
                elif char == 'E':
                    state = 36
                else:
                    state = 35
            case 35:
                if char != None: lookahead(file)
                c -= 1
                return Token("CONST_FRAC", temp[:-1], l, c)
            case 36:
                char = prox(file)
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char == '+-':
                    state = 37
                elif char != None and char in '0123456789':
                    state = 38
                else:
                    raise Exception()
            case 37:
                char = prox(file)
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char != None and char in '0123456789':
                    state = 38
                else:
                    raise Exception()
            case 38:
                char = prox(file)
                c += 1
                if char != None: temp+=char 
                else: temp+=" "
                if char != None and char in '0123456789':
                    state = 38
                else:
                    state = 39
            case 39:
                if char != None: lookahead(file)
                c -= 1
                return Token("CONST_EXP", temp[:-1], l, c)
            case 40:
                return Token("(", None, l, c)
            case 41:
                return Token(")", None, l, c)
            case 42:
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
                    state = 42
                else:
                    state = 43
            case 43:
                if char != None: lookahead(file)
                c -= 1
                state = 1 
            case _:
                break; #erro