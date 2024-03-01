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
                char = buffer.next_char

                if char == char.isalpha() or char == char.isdigit():
                    state = 2
                else:
                    state = 3
            case 3:
                
                return
            case 4:
                return
            case 5:
                return
            case 6:
                return
            case 7:
                char = buffer.next_char

                if char == '%':
                    state = 8
                else:
                    state = 7 
            case 8:
                return
            case 9:
                char = buffer.next_char

                if char == '=':
                    state = 10
                else:
                    return InappropriateCharacterException(char)
            case 10:
                return
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
                return
            case 13:
                return
            case 14:
                char - buffer.next_char

                if char == '-':
                    state = 15
                else:
                    return InappropriateCharacterException(char)
            case 15:
                return
            case 16:
                char = buffer.next_char

                if char == '=':
                    state = 17
                else:
                    state = 18
            case 17:
                return
            case 18:
                return
            case 19:
                return
            case 20:
                return
            case 21:
                char = buffer.next_char

                if char == '/':
                    state = 22
                else:
                    state = 23
            case 22:
                return
            case 23:
                return
            case 24:
                char = buffer.next_char

                if char == '*':
                    state = 25
                else:
                    state = 26
            case 25:
                return
            case 26:
                return
            case 27:
                return
            case 28:
                char = buffer.next_char  

                if char != "'":
                    state = 29
                else:
                    return InappropriateCharacterException(char)
            case 29:
               if char == "'":
                   state = 30
               else:
                   return InappropriateCharacterException(char)
            case 30:
                return
            case 31:
                char = buffer.next_char

                if char == char.isdigit():
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
                return
            case 37:
                char = buffer.next_char

                if char == char.isdigit():
                    state = 38
                else:
                    return InappropriateCharacterException(char)
            case 38:
                char = buffer.next_char

                if char == char.isdigit():
                    state = 38
                else:
                    state = 39
            case 39:
                return
            case 40:
                return
            case 41:
                return
            case 42:
                char = buffer.next_char

                if char == " " or char == '\t' or char == '\n':
                    state = 42
                else:
                    state = 43
            case 43:
                return
            case _:
                return
