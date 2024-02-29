class Point:
    init: int
    prox: int
    line: int
    column: int

    def __init__(self) -> None:
        self.init = -1
        self.prox = -1
        self.column = 1
        self.line = 1

    @property
    def location(self):
        return (self.line, self.column)

    def update_location(self, lexem: str):
        lex_lines = lexem.split("\n")
        self.line += max(len(lex_lines) - 1, 0)
        if len(lex_lines) > 1:
            self.column = 1
        self.column += len(lex_lines[-1])

    @property
    def position(self):
        return (self.init, self.prox)

    def step_look_ahead(self):
        self.prox += 1

    def handle_look_ahead(self):
        self.prox -= 1

    def init_take_prox(self):
        self.init = self.prox - 1
        self.prox = self.init