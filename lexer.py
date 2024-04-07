from enum import Enum

class TokenType(Enum):
    LEFT_BRACE = 1


class Token:
    def __init__(self, tt: TokenType, lexeme: str) -> None:
        self.tt = tt
        self.literal = lexeme

    def __repr__(self) -> str:
        return f"{self.tt}, {self.literal}"

class Lexer:
    def __init__(self, source) -> None:
        self.source = source
        self.start_position = 0
        self.current_position = 0

        self.tokens: list = []

    def consume_characters(self) -> None:
        while not self.isAtEnd():
            self.start_position = self.current_position
            self._consume_character()

    def _consume_character(self) -> None:
        c: str = self.eat_and_move_on()
        if c == "{":
            self.generate_and_add_token(TokenType.LEFT_BRACE.name)

    def generate_and_add_token(self, tt: TokenType) -> None:
        text: str = self.source[self.start_position:self.current_position]
        token = Token(tt, text)
        self.tokens.append(token)

    def eat_and_move_on(self) -> str:
        self.current_position = self.current_position + 1
        return self.source[self.current_position - 1]

    def isAtEnd(self) -> bool:
        return self.current_position >= len(self.source)

if __name__ == "__main__":
    source: str = "{"
    lexer = Lexer(source)
    lexer.consume_characters()