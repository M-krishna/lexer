from enum import Enum

class TokenType(Enum):
    LEFT_BRACE = 1
    RIGHT_BRACE = 2
    LEFT_PAREN = 3
    RIGHT_PAREN = 4
    STAR = 5
    PLUS = 6
    MINUS = 7
    COMMA = 8
    DOT = 9

class Token:
    def __init__(self, tt: TokenType, lexeme: str) -> None:
        self.token_type = tt
        self.lexeme = lexeme

    def __repr__(self) -> str:
        return f"{self.token_type} {self.lexeme}"

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
        current_character: str = self.eat_and_move_on()

        if current_character == '{':
            self.generate_and_add_token(TokenType.LEFT_BRACE.name)
        if current_character == '}':
            self.generate_and_add_token(TokenType.RIGHT_BRACE.name)
        if current_character == '(':
            self.generate_and_add_token(TokenType.LEFT_PAREN.name)
        if current_character == ')':
            self.generate_and_add_token(TokenType.RIGHT_PAREN.name)
        if current_character == '*':
            self.generate_and_add_token(TokenType.STAR.name)
        if current_character == '+':
            self.generate_and_add_token(TokenType.PLUS.name)
        if current_character == '-':
            self.generate_and_add_token(TokenType.MINUS.name)
        if current_character == ',':
            self.generate_and_add_token(TokenType.COMMA.name)
        if current_character == '.':
            self.generate_and_add_token(TokenType.DOT.name)

    def generate_and_add_token(self, tt: TokenType) -> None:
        text: str = self.source[self.start_position:self.current_position]
        token = Token(tt, text)
        self.tokens.append(token)

    def eat_and_move_on(self) -> str:
        self.current_position = self.current_position + 1
        return self.source[self.current_position - 1]

    def isAtEnd(self) -> bool:
        return self.current_position >= len(self.source)

    def print_tokens(self) -> None:
        print(self.tokens)

if __name__ == "__main__":
    source: str = "{}{}{}()+-*,."
    lexer = Lexer(source)
    lexer.consume_characters()
    lexer.print_tokens()