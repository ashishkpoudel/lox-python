from lox_python.token import Token
from lox_python.token_type import TokenType

class Scanner:
  def __init__(self, source: str):
    self.source = source
    self.tokens: list[Token] = []
    self.start = 0
    self.current = 0
    self.line = 1
    self.keywords = {
      "and": TokenType._and,
      "class": TokenType._class,
      "else": TokenType._else,
      "false": TokenType._flase,
      "for": TokenType._for,
      "fun": TokenType._fun,
      "if": TokenType._if,
      "nil": TokenType._nil,
      "or": TokenType._or,
      "print": TokenType._print,
      "return": TokenType._return,
      "super": TokenType._super,
      "this": TokenType._this,
      "var": TokenType._var,
      "while": TokenType._while,
    }

  def scan_tokens(self):
    while not self.is_at_end():
      self.start = self.current
      self.scan_token()

    self.tokens.append(Token(TokenType._eof, "", None, self.line))
    
    return self.tokens

  def scan_token(self):
    char = self.advance()
    print("char: {char}".format(char = char))
    match char:
      case "(":
        self.add_token(TokenType._left_paren)
      case ")":
        self.add_token(TokenType._right_paren)
      case "{":
        self.add_token(TokenType._left_brace)
      case "}":
        self.add_token(TokenType._right_brace)
      case ",":
        self.add_token(TokenType._comma)
      case ".":
        self.add_token(TokenType._dot)
      case "-":
        self.add_token(TokenType._minus)
      case "+":
        self.add_token(TokenType._plus)
      case ";":
        self.add_token(TokenType._semicolon)
      case "*":
        self.add_token(TokenType._star)
      case "!":
        self.add_token(TokenType._bang_equal if self.match("=") else TokenType._bang)
      case "=":
        self.add_token(TokenType._equal_equal if self.match("=") else TokenType._equal)
      case "<":
        self.add_token(TokenType._less_equal if self.match("=") else TokenType._less)
      case ">":
        self.add_token(TokenType._greater_equal if self.match("=") else TokenType._greater)
      case "/":
        if self.match("/"):
          # A comment goes until the end of the line
          while self.peek() != "\n" and not self.is_at_end():
            self.advance()
        else:
          self.add_token(TokenType._slash)
      case "\n":
        self.line += 1
      case '"':
        self.string()
      case _:
        if self.is_digit(char):
          self.number()
        elif self.is_alpha(char):
          self.identifier()
        else:
          print("Unexpected character in line: {line}".format(line = self.line))

  def is_digit(self, value: str):
    if value >= '0' and value <= '9':
      return True

  def number(self):
    while self.is_digit(self.peek()):
      self.advance()
    
    # look for a fractional part
    if self.peek() == "." and self.is_digit(self.peek_next()):
      self.advance()

      while self.is_digit(self.peek()):
        self.advance()

    numberLike = self.source[self.start, self.current]
    self.add_token(TokenType._number, int(numberLike))

  def string(self):
    while self.peek() != '"' and not self.is_at_end():
      if self.peek() == "\n":
        self.line += 1

      self.advance()

    if self.is_at_end():
      print("Unterminated string {line}".format(line = self.line))
      return
    
    self.advance()

    # trim the surrounding quotes
    value = self.source[self.start + 1:self.current - 1]
    self.add_token(TokenType._string, value)

  def match(self, value: str):
    if self.is_at_end():
      return False

    if self.source[self.current] is not value:
      return False

    self.current += 1
    return True

  def add_token(self, type: TokenType, literal: dict[str, any] | None = None):
    text = self.source[self.start:self.current]
    self.tokens.append(Token(type, text, literal, self.line))

  def advance(self):
    self.current += 1
    return self.source[self.current - 1]

  def peek(self):
    if self.is_at_end():
      return "\0"
    
    return self.source[self.current]

  def peek_next(self):
    if self.current + 1 >= len(self.source):
      return "\0"
    
    return self.source[self.current + 1]

  def is_at_end(self):
    return self.current >= len(self.source)

  def is_alpha(self, char: str):
    return (char >= "a" and char <= "z") or (char >= "A" and char <= "Z") or char == "_"

  def is_alpha_numeric(self, char: str):
    return self.is_alpha(char) or self.is_digit(char)
  
  def identifier(self):
    while self.is_alpha_numeric(self.peek()):
      self.advance()
    
    text = self.source[self.start:self.current]
    type = self.keywords[text]

    self.add_token(type if type else TokenType._identifier)
  
