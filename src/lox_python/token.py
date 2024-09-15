from lox_python.token_type import TokenType

class Token:
  def __init__(self, type: TokenType, lexeme: str, literal: dict[str, any], line: int):
    self.type = type
    self.lexeme = lexeme
    self.literal = literal
    self.line = line

  def to_string(self):
    return "{type} {lexeme}".format(type = self.type, lexeme = self.lexeme)
  
