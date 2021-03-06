# ==============================================================================
"""SQUARES : print the sequence of square numbers from 1*1 to n*n"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "1.0" # use 'while' loop to generate string
__date__    = "2018-01-15"
__usage__   = """
User input: <n> (where n:int > 0)
App output: sequence of square numbers from 1*1 to n*n"""
# ==============================================================================
from ezCLI import *
# ------------------------------------------------------------------------------
def square(n):
  """return the square of 'n'"""
  return n*n
# ------------------------------------------------------------------------------
def squares(n):
  """return a string containing the 'n' first square numbers"""
  p, lines = 1, ''
  while (p <= n):
    lines += f"{p} * {p} = {square(p)}\n"
    p += 1; #inspect()
  return lines.strip() # remove trailing newline character
# ------------------------------------------------------------------------------
def parser(command):
  """parse 'command' as integer 'n' before calling 'squares(n)'"""
  n = parse(command); #inspect()
  assert type(n) is int and n > 0, "<n> must be a strictly positive integer"
  return squares(n)
# ==============================================================================
if __name__ == '__main__':
  userloop(parser, "Enter value for <n>")
# ==============================================================================
