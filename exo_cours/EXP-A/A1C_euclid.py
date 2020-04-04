# ==============================================================================
"""EUCLID : compute the Euclidian division of two integer numbers"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "3.0" # add command line for user input
__date__    = "2018-01-15"
# ==============================================================================
command = input("<> Enter <numerator> <denominator> : ")
a, b = command.split() # split command line into words
a, b = int(a), int(b)
print(f"{a} = {b} * {a//b} + {a%b}")
# ==============================================================================
