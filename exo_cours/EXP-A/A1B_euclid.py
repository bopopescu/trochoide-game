# ==============================================================================
"""EUCLID : compute the Euclidian division of two integer numbers"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "2.0" # add interactive user input
__date__    = "2018-01-15"
# ==============================================================================
a = input("<> Value of numerator : ")
b = input("<> Value of denominator : ")
print(type(a), type(b)) # 'a' and 'b' are strings
a, b = int(a), int(b)
print(type(a), type(b)) # 'a' and 'b' have been converted to integers
print(f"{a} = {b} * {a//b} + {a%b}")
# ==============================================================================
