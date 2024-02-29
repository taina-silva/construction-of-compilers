from src.utils.point import Point

BUFFER_SIZE = 8192
DEBUG = False

class Buffer:
    buffer_pair: list[str]
    current_buffer: int
    scan_point: Point
    buffer_num: int
    _has_swaped: bool
    file = str

    def __init__(self, file="") -> None:
        self.buffer_pair = [[], []]
        self.current_buffer = 0
        self.buffer_num = 0
        self.scan_point = Point()
        self.file = file
        self.load(file=file)
        self._has_swaped = False

    def change(self) -> None:
        self.scan_point.prox = -1
        self._has_swaped = True
        self.current_buffer = (self.current_buffer + 1) % 2

    @property
    def next_char(self) -> str | None:
        """Retorna o próximo caracter no buffer, lidando com a troca de buffers (sentinelas)"""

        self.scan_point.step_look_ahead()
        next_char = self.buffer_pair[self.current_buffer][self.scan_point.prox]

        if next_char == "$":
            #  Pode ser sentinela padrão ou pode ser final de arquivo
            if self.scan_point.prox == BUFFER_SIZE - 1:
                # Sentinela padrão (final de buffer)
                self.change()
                self.load(file=self.file)
            # else: FIM DE ARQUIVO
        return next_char

    def load(self, file: str) -> None:
        with open(file, "r", encoding="utf-8") as file_code:
            # move pointer for where to read
            file_code.seek(self.buffer_num * BUFFER_SIZE)
            self.buffer_num += 1

            buffer_ = file_code.read(BUFFER_SIZE - 1)
            buffer_ = buffer_ + "$"
            # Nao apagar linha abaixo talvez seja bom para testes
            # buffer = repr(buffer)
            self.buffer_pair[self.current_buffer] = buffer_

    def sync(self, handle_lookahead: bool = False) -> str:
        """
        Retorna o lexema definido pelos ponteiros 'init' e 'prox' e o seu "Point" de início,
        lidando com lookahead se necessário, e preparando os ponteiros para continuar a análise léxica.
        """
        if handle_lookahead:
            self.scan_point.handle_look_ahead()

        lexem = ""

        if self._has_swaped:
            old_buffer = (self.current_buffer + 1) % 2
            first_part = self.buffer_pair[old_buffer][
                (self.scan_point.init + 1) : (BUFFER_SIZE)
            ]
            last_part = self.buffer_pair[self.current_buffer][0 : self.scan_point.prox]
            lexem = first_part + last_part
            self._has_swaped = False
        else:
            lexem = self.buffer_pair[self.current_buffer][
                (self.scan_point.init + 1) : self.scan_point.prox
            ]
        self.scan_point.init_take_prox()
        self.scan_point.update_location(lexem)
        return lexem