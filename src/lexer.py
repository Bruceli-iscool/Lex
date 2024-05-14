"""Generate Lexer Object"""
import re


class Lexer:
    """Lexer Object"""
    def __init__(self, tokens_list:tuple):
        # take tuple as input.
        self.tokens = tokens_list
        self.position = 0
    def lex(self, user_input:str):
        return list(self.lexer(user_input))
    def lexer(self, user_input:str):
        # actual lexing happens here.
        while self.position < len(user_input):
            match = None
            for token_type in self.tokens:
                token_name, pattern = token_type
                regex = re.compile(pattern)
                match = regex.match(user_input, self.position)
                if match:
                    value = match.group(0)
                    yield (token_name, value)
                    self.position = match.end()
                    break
            if not match:
                    # Skip whitespace characters
                    if user_input[self.position].isspace():
                        self.position += 1
                        continue
                    else:
                        raise ValueError

