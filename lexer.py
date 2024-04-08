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

    BANG = 10
    BANG_EQUAL = 11
    EQUAL = 12
    EQUAL_EQUAL = 13
    LESS_THAN = 14
    LESS_THAN_EQUAL = 15
    GREATER_THAN = 16
    GREATER_THAN_EQUAL = 17

    # Keywords
    AND = 18
    OR = 19
    NOT = 20
    IF = 21
    ELIF = 22
    ELSE = 23
    WHILE = 24
    FOR = 25
    BREAK = 26
    CONTINUE = 27
    DEF = 28
    RETURN = 29
    CLASS = 30
    PRINT = 31

class Token:
    def __init__(self, tt: TokenType, value: str) -> None:
        self.token_type = tt
        self.value = value

    def __repr__(self) -> str:
        return f"{self.token_type} {self.value}"

class Lexer:

    KEYWORDS = {
        "and": TokenType.AND.name,
        "or": TokenType.OR.name,
        "not": TokenType.NOT.name,
        "if": TokenType.IF.name,
        "elif": TokenType.ELIF.name,
        "else": TokenType.ELSE.name,
        "while": TokenType.WHILE.name,
        "for": TokenType.FOR.name,
        "break": TokenType.BREAK.name,
        "continue": TokenType.CONTINUE.name,
        "def": TokenType.DEF.name,
        "return": TokenType.RETURN.name,
        "class": TokenType.CLASS.name,
        "print": TokenType.PRINT.name
    }

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
        if self.isWhitespace(current_character):
            return
        if current_character == '!':
            self.generate_and_add_token(
                TokenType.BANG_EQUAL.name if self.match_next_character('=') else TokenType.BANG.name
            )
        if current_character == '=':
            self.generate_and_add_token(
                TokenType.EQUAL_EQUAL.name if self.match_next_character('=') else TokenType.EQUAL.name
            )
        if current_character == '<':
            self.generate_and_add_token(
                TokenType.LESS_THAN_EQUAL.name if self.match_next_character('=') else TokenType.LESS_THAN.name
            )
        if current_character == '>':
            self.generate_and_add_token(
                TokenType.GREATER_THAN_EQUAL.name if self.match_next_character('=') else TokenType.GREATER_THAN.name
            )

        if current_character.isalpha():
            while (self.peek().isalpha()):
                self.eat_and_move_on()
            keyword: str = self.source[self.start_position:self.current_position]
            self.generate_and_add_token(
                Lexer.KEYWORDS.get(keyword, None)
            )


    def generate_and_add_token(self, tt: TokenType) -> None:
        text: str = self.source[self.start_position:self.current_position]
        token = Token(tt, text)
        self.tokens.append(token)

    def eat_and_move_on(self) -> str:
        self.current_position = self.current_position + 1
        return self.source[self.current_position - 1]

    def match_next_character(self, expected_character: str) -> bool:
        if self.isAtEnd(): return False
        if (self.source[self.current_position] != expected_character): return False
        
        # Since its a match we have to consume(eat) the character.
        # That is why we are incrementing the current_position value
        self.current_position = self.current_position + 1
        return True

    def peek(self) -> chr:
        if self.isAtEnd(): return '\0'
        return self.source[self.current_position]

    def isAtEnd(self) -> bool:
        return self.current_position >= len(self.source)

    def isWhitespace(self, c: str) -> bool:
        SPACE = ' '
        NEWLINE = '\n'
        CARRIAGE_RETURN = '\r'
        return c in [SPACE, NEWLINE, CARRIAGE_RETURN]

    def print_tokens(self) -> None:
        print(self.tokens)

if __name__ == "__main__":
    source: str = "and or not if elif else while for break continue def return class print orand"
    lexer = Lexer(source)
    lexer.consume_characters()
    lexer.print_tokens()