from enum import Enum

class TokenType(Enum):
  # single character tokens..
  _left_paren = "left_paren"
  _right_paren = "right_paren"
  _left_brace = "left_brace"
  _right_brace = "right_brace"
  _comma = "comma"
  _minus = "minus"
  _plus = "plus"
  _semicolon = "semicolon"
  _slash = "slash"
  _star = "star"
  
	# one or two character tokens
  _bang = "bang"
  _bang_equal = "bang_equal"
  _equal = "equal"
  _equal_equal = "equal_equal"
  _less = "less"
  _less_equal = "less_equal"
  _greater = "greater"
  _greater_equal = "greater_equal"
  
	# literals
  _identifier = "identifier"
  _string = "string"
  _number = "number"
  
	# keywords
  _and = "and"
  _class = "class"
  _else = "else"
  _flase = "false"
  _fun = "fun"
  _for = "for"
  _if = "if"
  _nil = "nil"
  _or = "or"
  _print = "print"
  _return = "return"
  _super = "super"
  _this = "this"
  _true = "true"
  _var = "var"
  _while = "while"
  _eof = "eof"
  _dot = "dot"

