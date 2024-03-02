import sys

from src.utils.buffer import Buffer
from src.exceptions.inappropriate_character_exception import InappropriateCharacterException
from src.utils.token import token as tk
from src.analyzers import symbol_table

buffer = Buffer(file=sys.argv[1])

class LexerError(Exception):
    """Errors on Lexer"""

    position: tuple[int, int]

    def __init__(self, position: tuple[int, int]) -> None:
        self.position = position


def operadores_relacionais_token(op_code: int) -> tk.Token:
    return tk.Token("operadores_relacionais", op_code)


def common_symbol(symbol: str) -> tk.Token:
    return tk.Token(symbol, None)


def set_id(identifier: str) -> tk.Token:
    position = symbol_table.lookup(identifier)
    if position is None:
        position = symbol_table.append(identifier, "ID", None, None)
    return tk.Token("ID", position)


def set_char(character: str) -> tk.Token:
    position = symbol_table.lookup(character)
    if position is None:
        position = symbol_table.append(
            lexemn=character, token_type="CONST_CHAR", value=character, data_type="char"
        )
    return tk.Token("CONST_CHAR", position)


def set_int(integer: str) -> tk.Token:
    position = symbol_table.lookup(integer)
    if position is None:
        position = symbol_table.append(
            lexemn=integer, token_type="CONST_NUM", value=integer, data_type="int"
        )
    return tk.Token("CONST_NUM", position)


def set_frac(fractional_nbr: str) -> tk.Token:
    position = symbol_table.lookup(fractional_nbr)
    if position is None:
        position = symbol_table.append(
            lexemn=fractional_nbr,
            token_type="CONST_NUM",
            value=fractional_nbr,
            data_type="float",
        )
    return tk.Token("CONST_NUM", position)


def set_exp(exp: str) -> tk.Token:
    position = symbol_table.lookup(exp)
    if position is None:
        position = symbol_table.append(
            lexemn=exp,
            token_type="CONST_NUM",
            value=exp,
            data_type="float",
        )
    return tk.Token("CONST_NUM", position)


def get_token():
    state = 1  # estado inicial 

    while True:
        match state:
            case 1:
                char = buffer.next_char

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
                elif char == char.isdigit():
                    state = 31
                elif char == '(':
                    state = 40
                elif char == ')':
                    state = 41
                elif char == " " or char == '\t' or char == '\n':
                    state = 42
                else:
                    return InappropriateCharacterException(char)
            case 2:
                char = buffer.next_char

                if char == char.isalpha() or char == char.isdigit():
                    state = 2
                else:
                    state = 3
            case 3:
                return
            case 4:
                location = buffer.scan_point.location
                return common_symbol(buffer.sync()), location
            case 5:
                location = buffer.scan_point.location
                return common_symbol(buffer.sync()), location
            case 6:
                location = buffer.scan_point.location
                return common_symbol(buffer.sync()), location
            case 7:
                char = buffer.next_char

                if char == '%':
                    state = 8
                else:
                    state = 7 
            case 8:
                buffer.sync()
                state = 1 #reinicia a função para ignorar comentários
            case 9:
                char = buffer.next_char

                if char == '=':
                    state = 10
                else:
                    return InappropriateCharacterException(char)
            case 10:
                location = buffer.scan_point.location
                buffer.sync()
                return operadores_relacionais_token(tk.operadores_relacionais_EQ), location
            case 11:
                char = buffer.next_char

                if char == '=':
                    state = 12
                elif char == '>':
                    state = 13
                elif char == '-':
                    state = 14
                else:
                    state = 21
            case 12:
                location = buffer.scan_point.location
                buffer.sync()
                return operadores_relacionais_token(tk.operadores_relacionais_LE), location
            case 13:
                location = buffer.scan_point.location
                buffer.sync()
                return operadores_relacionais_token(tk.operadores_relacionais_NE), location
            case 14:
                char = buffer.next_char

                if char == '-':
                    state = 15
                else:
                    return InappropriateCharacterException(char)
            case 15:
                location = buffer.scan_point.location
                return common_symbol(buffer.sync()), location
            case 16:
                char = buffer.next_char

                if char == '=':
                    state = 17
                else:
                    state = 18
            case 17:
                location = buffer.scan_point.location
                buffer.sync()
                return operadores_relacionais_token(tk.operadores_relacionais_GE), location
            case 18:
                location = buffer.scan_point.location
                buffer.sync(handle_lookahead = True)
                return operadores_relacionais_token(tk.operadores_relacionais_GT), location
            case 19:
                location = buffer.scan_point.location
                return common_symbol(buffer.sync()), location
            case 20:
                location = buffer.scan_point.location
                return common_symbol(buffer.sync()), location
            case 21:
                char = buffer.next_char

                if char == '/':
                    state = 22
                else:
                    state = 23
            case 22:
                location = buffer.scan_point.location
                return common_symbol(buffer.sync()), location
            case 23:
                location = buffer.scan_point.location
                buffer.sync(handle_lookahead=True)
                return common_symbol(buffer.sync()), location
            case 24:
                char = buffer.next_char

                if char == '*':
                    state = 25
                else:
                    state = 26
            case 25:
                location = buffer.scan_point.location
                return common_symbol(buffer.sync()), location
            case 26:
                location = buffer.scan_point.location
                buffer.sync(handle_lookahead=True)
                return common_symbol(buffer.sync()), location
            case 27:
                location = buffer.scan_point.location
                return common_symbol(buffer.sync()), location
            case 28:
                char = buffer.next_char  

                if char != "'":
                    state = 29
                else:
                    return InappropriateCharacterException(char)
            case 29:
               char = buffer.next_char 

               if char == "'":
                   state = 30
               else:
                   return InappropriateCharacterException(char)
            case 30:
                return
            case 31:
                char = buffer.next_char

                if char.isdigit():
                    state = 31
                elif char == '.':
                    state = 33
                elif char == 'E':
                    state = 36
                else:
                    state = 32
            case 32:
                return
            case 33:
                char = buffer.next_char

                if char == char.isdigit():
                    state = 34
                else:
                    return InappropriateCharacterException(char)
            case 34:
                char = buffer.next_char

                if char == char.isdigit():
                    state = 34
                elif char == 'E':
                    state = 36
                else:
                    state = 35
            case 35:
                return
            case 36:
                char = buffer.next_char

                if char == '+-':
                    state = 37
                elif char == char.isdigit():
                    state = 38
                else:
                    return InappropriateCharacterException(char)
            case 37:
                char = buffer.next_char

                if char.isdigit():
                    state = 38
                else:
                    return InappropriateCharacterException(char)
            case 38:
                char = buffer.next_char

                if char.isdigit():
                    state = 38
                else:
                    state = 39
            case 39:
                return
            case 40:
                location = buffer.scan_point.location
                return common_symbol(buffer.sync()), location
            case 41:
                location = buffer.scan_point.location
                return common_symbol(buffer.sync()), location
            case 42:
                char = buffer.next_char

                if char == " " or char == '\t' or char == '\n':
                    state = 42
                else:
                    state = 43
            case 43:
                buffer.sync(handle_lookahead=True)
                state = 1  
            case _:
                break; #erro