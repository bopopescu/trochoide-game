# ==============================================================================
"""MULTABLE : print the multiplication table from 1*1 to n*n"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "2.0" # use embedded list comprehension to generate table
__date__    = "2018-01-15"
__usage__   = """
User input: <n> (where n:int > 0)
App output: multiplication table from 1*1 to n*n"""
# ==============================================================================
from ezCLI import *
# ------------------------------------------------------------------------------
def multable(n):
  """return a string containing the multiplication table from 1*1 to n*n"""
  # create 'table' as a matrix of 3-character strings
  table = [[f"{p*q:3}" for q in range(1, n+1)] for p in range(1, n+1)]
  # join each line from 'table' into a single string
  lines = [' '.join(line) for line in table]; #inspect()
  return '\n'.join(lines) # join all lines into a multi-line string
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
