class Tag(object):
    identificador: str
    def __init__(self, tag, eh_terminal):
        self.tag = tag
        self.eh_terminal = eh_terminal

class Tabelas(object):
    def __init__(self, lista=[]):
        self.tabela_producoes = {}
        for lp in lista:
            self.tabela_producoes[lp[0]] = []
            for p in lp[1]:
                self.tabela_producoes[lp[0]].append(Tag(p[0], p[1]))
                
        self.tabela_preditiva = {
            "<inicio>": {"programa": "P2"},
            "<bloco>": {"/*": "P3"},
            "<declaracao_vars>": {"int": "P4", "float": "P4", "char": "P4", "ID": "P1", "enquanto": "P1", "repita": "P1", "se": "P1", "*/": "P1"},
            "<declaracao_var>": {"int": "P5", "float": "P5", "char": "P5"},
            "<tipo>": {"int": "P6", "char": "P7", "float": "P8"},
            "<lista_ids>": {"ID": "P9"},
            "<lista_ids'>": {",": "P10", ";": "P1"},
            "<comandos>": {"ID": "P11", "enquanto": "P11", "repita": "P11", "se": "P11", "*/": "P1"},
            "<comando>": {"ID": "P12", "enquanto": "P13", "repita": "P14", "se": "P15"},
            "<comando_atribuicao>": {"ID": "P16"},
            "<comando_repeticao1>": {"enquanto": "P17"},
            "<comando_repeticao2>": {"repita": "P18"},
            "<comando_selecao>": {"se": "P19"},
            "<comando_selecao'>": {"senao": "P20", "ID": "P1", "enquanto": "P1", "repita": "P1", "se": "P1", "*/": "P1", "ate": "P1"},
            "<comando_ou_bloco>": {"ID": "P21", "enquanto": "P21", "repita": "P21", "se": "P21", "/*": "P22"},
            "<condicao>": {"(": "P23", "CONST_CHAR": "P23", "CONST_NUM": "P23", "ID": "P23"},
            "<expressao>": {"(": "P24", "CONST_CHAR": "P24", "CONST_NUM": "P24", "ID": "P24"},
            "<expressao'>": {"+": "P25", "-": "P26", "relop": "P1", ")": "P1", ";": "P1"},
            "<termo>": {"(": "P27", "CONST_CHAR": "P27", "CONST_NUM": "P27", "ID": "P27"},
            "<termo'>": {"*": "P28", "/": "P29", "+": "P1", "-": "P1", "relop": "P1", ")": "P1", ";": "P1"},
            "<expo>": {"(": "P30", "CONST_CHAR": "P30", "CONST_NUM": "P30", "ID": "P30"},
            "<expo'>": {"^": "P31", "*": "P1", "/": "P1", "+": "P1", "-": "P1", "relop": "P1", ")": "P1", ";": "P1"},
            "<fator>": {"(": "P32", "CONST_CHAR": "P33", "CONST_NUM": "P34", "ID": "P35"}
        }