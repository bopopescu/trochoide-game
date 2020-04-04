# ==============================================================================
"""MULTABLE : print the multiplication table from 1*1 to n*n"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "1.0" # use two embedded 'for' loops to generate table
__date__    = "2018-01-15"
__usage__   = """
User input: <n> (where n:int > 0)
App output: multiplication table from 1*1 to n*n"""
# ==============================================================================
from ezCLI import *
# ------------------------------------------------------------------------------
def multable(n):
  """return a string containing the multiplication table from 1*1 to n*n"""
  lines = ''
  for p in range(1, n+1):
    for q in range(1, n+1): 
      lines += f" {p*q:3}"; #inspect() # string length is forced to 3 chars
    lines += '\n'
  return lines.strip('\n') # remove trailing newline character
# ------------------------------------------------------------------------------
def parser(command):
  """parse 'command' as integer 'n' before calling 'multable(n)'"""
  n = parse(command); #inspect()
  assert type(n) is int and n > 0, "<n> must be a strictly positive integer"
  return multable(n)
# ==============================================================================
if __name__ == '__main__':
  userloop(parser, "Enter value for <n>")
# ==============================================================================
