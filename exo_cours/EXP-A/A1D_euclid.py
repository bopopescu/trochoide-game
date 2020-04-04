# ==============================================================================
"""EUCLID : compute the Euclidian division of two integer numbers"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "4.0" # add interaction loop
__date__    = "2018-01-15"
# ==============================================================================
print("Note: enter empty line to stop interaction loop\n")
while True:
  command = input("<> Enter <numerator> <denominator> : ")
  if command == '': break # break loop when user enter an empty line
  a, b = command.split()
  a, b = int(a), int(b)
  print(f"{a} = {b} * {a//b} + {a%b}")
#print("See you later...")
# ==============================================================================
