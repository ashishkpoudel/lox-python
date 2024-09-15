import sys
from lox_python.scanner import Scanner

class Lox:
  def __init__(self):
    self.had_error = False

  def main(self):
    if len(sys.argv) == 1:
      self.run_prompt()
    elif len(sys.argv) == 2:
      file_name = sys.argv[1]
      self.run_file(file_name)
    else:
      usage_doc = "Usage: lox.py [script]"
      print(usage_doc)
      sys.exit(64)

  def run_prompt(self):
    while True:
      line = input("> ")
      if not line:
        break

      self.run(line)
      self.had_error = False

  def run_file(self, input_file: str):
    with open(input_file, "r") as source_file:
      self.run(source_file.read())

    if (self.had_error):
      sys.exit(65)

  def run(self, source: str):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()

    for token in tokens:
      print(token.to_string())

  def error(self, line: int, message: str):
    self.report(line, "", message)

  def report(self, line: int, where: str, message: str):
    message = "[line {line}] Error {where} : {message}".format(
      line = line, where = where, message = message
    )

    self.had_error = True

lox = Lox()
lox.main()
