import sys

from utils.token import Token

class entry_symbol_table:
    token_type: str
    lexemn: str
    token_value: int
    data_type: str

    def __init__(
            self, token_type,  lexemn, token_value, data_type):
        self.lexemn, self.token_type, self.token_value, self.data_type

    def __repr__(self) -> str:
        return f"entry_symbol_table({self.token_type}, {self.lexemn}, {self.token_value}, {self.data_type})"

class symbol_table:
    table: list[entry_symbol_table]
    key: list[str]

    def __init__(self) -> None:
        #(tipo do token, lexema, valor do token, tipo do dado) 

        self.table = [
            entry_symbol_table("programa", "programa", None, None),
            entry_symbol_table("int", "int", None, None),
            entry_symbol_table("char", "char", None, None),
            entry_symbol_table("float", "float", None, None),
            entry_symbol_table("se", "se", None, None),
            entry_symbol_table("entao", "entao", None, None),
            entry_symbol_table("senao", "senao", None, None),
            entry_symbol_table("enquanto", "enquanto", None, None),
            entry_symbol_table("faca", "faca", None, None),
            entry_symbol_table("repita", "repita", None, None),
            entry_symbol_table("ate", "ate", None, None),
        ]  
        
        self.key = [
            "programa", "int", "char", "float", "se", "entao", "senao", "enquanto", "faca", "repita", "ate"]
        
    def append(self, token_type: str, lexemn: str, token_value: any, data_type: str) -> int:
        entry_symbol = entry_symbol_table(token_type, lexemn, token_value, data_type)
        self.table.append(entry_symbol)
        return len(self.table)-1
        
    #verifica se um lexema já está presente na tabela
    def lookup(self, lexemn: str) -> int | None:
        for i, entry in enumerate(self.table):
            if entry.lexemn == lexemn:
                return i
        return None
