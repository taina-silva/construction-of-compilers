OPERADORES_RELACIONAIS_LT = 1
OPERADORES_RELACIONAIS_LE = 2
OPERADORES_RELACIONAIS_EQ = 3
OPERADORES_RELACIONAIS_NE = 4
OPERADORES_RELACIONAIS_GT = 5
OPERADORES_RELACIONAIS_GE = 6


class Token:
    token_type: str
    token_attribute: int | None

    def __init__(self, token_type, token_attribute):
        self.token_type = token_type
        self.token_attribute = token_attribute

    def __repr__(self) -> str:
        return f"TOKEN<{self.token_type}, {self.token_attribute}>"