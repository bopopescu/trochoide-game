# ==============================================================================
"""EUCLID : compute the Euclidian division of two integer numbers"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "6.0" # use 'userloop/parse/inspect' from the 'ezCLI' module
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
  """parse 'command' as two integers and return Euclidian decomposition"""
  a, b = parse(command); #inspect()
  return euclid(a, b)
# ==============================================================================
if __name__ == '__main__':
  userloop(parser, "Enter <numerator> <denominator>") # user interaction loop
# ==============================================================================
