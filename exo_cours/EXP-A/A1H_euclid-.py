# ==============================================================================
"""EUCLID : compute the Euclidian division of two integer numbers"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "8.0" # add 'testcode' to check all use cases
__date__    = "2018-01-15"
__usage__   = """
User input: <numerator>,<denominator> (where numerator:int, denominator:int > 0)
App output: Euclidian division: numerator = denominator*q + r"""
# ==============================================================================
from ezCLI import *
# ------------------------------------------------------------------------------
def euclid(a,b):
  """return Euclidian decomposition: a = b*q + r"""
  return f"{a} = {b} * {a//b} + {a%b}"
# ------------------------------------------------------------------------------
def parser(command):
  """parse 'command' as two integers 'a,b' and return Euclidian decomposition"""
  command = parse(command); #inspect()
  assert len(command) == 2, "two space-separated arguments are required"
  a, b = command; #inspect()
  assert type(a) is int, "numerator must be an integer"
  assert type(b) is int and b > 0, "denominator must be a positive integer"
  return euclid(a,b)
# ==============================================================================
if __name__ == '__main__':
  #userloop(parser, "Enter <numerator> <denominator>")

  code = r"""
# ------------------------------------------------------------------------------
# Test euclid(a,b)
# ------------------------------------------------------------------------------
euclid(0,1)
euclid(1,1)
euclid(-1,1)
euclid(7,3)
euclid(-7,3)

# ------------------------------------------------------------------------------
# Test parser(command)
# ------------------------------------------------------------------------------
parser('')
parser(',')
parser('1')
parser('1 a')
parser('a 1')
parser('1 1 1')

parser('1.0 1')
parser('1 1.0')
parser('1 0')
parser('1 -1')

parser('1 1')
parser('   1     1   ')
parser('0 1')
parser('-1 1')
parser('7 3')
parser('-7 3')
"""; testcode(code)
# ==============================================================================
