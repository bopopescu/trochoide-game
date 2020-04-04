# ==============================================================================
"""EUCLID : compute the Euclidian division of two integer numbers"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "5.0" # split code into kernel and interface functions
__date__    = "2018-01-15"
# ==============================================================================
def euclid(x,y):
  """return Euclidian decomposition: a = b*q + r"""
  return f"{x} = {y} * {x//y} + {x%y}"
# ------------------------------------------------------------------------------
def parser(command):
  """parse 'command' as two integers 'a,b' and return Euclidian decomposition"""
  a, b = command.split()
  a, b = int(a), int(b)
  return euclid(a, b)
# ------------------------------------------------------------------------------
def loop():
  """interaction loop for the "euclid" module"""
  print("Note: enter empty line to stop interaction loop\n")
  while True:
    command = input("<> Enter <numerator> <denominator> : ")
    if command == '': break
    print(parser(command))
  print("See you later...")
# ==============================================================================
if __name__ == '__main__': # test whether this code is used as module or program
  loop()
# ==============================================================================
