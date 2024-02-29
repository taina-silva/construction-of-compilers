class InappropriateCharacterException(Exception):
    """
    Exception for cases when character is not expected
    """

    char: str

    def __init__(self, character):
        self.char = character