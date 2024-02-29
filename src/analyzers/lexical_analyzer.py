import sys

from src.utils.buffer import Buffer
from src.exceptions.inappropriate_character_exception import InappropriateCharacterException

buffer = Buffer(file=sys.argv[1])

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
                return
            case 3:
                return
            case 4:
                return
            case 5:
                return
            case 6:
                return
            case 7:
                return
            case 8:
                return
            case 9:
                return
            case 10:
                return
            case 11:
                return
            case 12:
                return
            case 13:
                return
            case 14:
                return
            case 15:
                return
            case 16:
                return
            case 17:
                return
            case 18:
                return
            case 19:
                return
            case 20:
                return
            case 21:
                return
            case 22:
                return
            case 23:
                return
            case 24:
                return
            case 25:
                return
            case 26:
                return
            case 27:
                return
            case 28:
                return
            case 29:
                return
            case 30:
                return
            case 31:
                return
            case 32:
                return
            case 33:
                return
            case 34:
                return
            case 35:
                return
            case 36:
                return
            case 37:
                return
            case 38:
                return
            case 39:
                return
            case 40:
                return
            case 41:
                return
            case 42:
                return
            case 43:
                return
            case _:
                return