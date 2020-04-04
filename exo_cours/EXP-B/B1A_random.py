# ==============================================================================
"""RANDOM : demo for some functions from the 'random' module"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "1.0"
__date__    = "2015-09-01"
__usage__   = """
Simply press <ENTER> at each pause""" 
# ==============================================================================
from ezCLI import *
from random import shuffle, choice, sample, randrange, random, gauss
# ------------------------------------------------------------------------------
# Shuffle a list of letters
# ------------------------------------------------------------------------------
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
pause("letters : %s" % letters)
test = list(letters); shuffle(test);
pause("shuffle : %s" % ''.join(test))
# ------------------------------------------------------------------------------
# Take random elements (with push back) from a list of letters
# ------------------------------------------------------------------------------
pause("choice : %s" % ' '.join(choice(letters) for n in range(20)))
# ------------------------------------------------------------------------------
# Take random elements (without push back) from a list of letters
# ------------------------------------------------------------------------------
pause("sample : %s" % ' '.join(sample(letters, 20)))
# ------------------------------------------------------------------------------
# Take random values from an integer range (0,100,5)
# ------------------------------------------------------------------------------
pause("randrange : %s" % [randrange(0, 100, 5) for n in range(15)])
# ------------------------------------------------------------------------------
# Histogram of the integer range selection for 100000 random values
# ------------------------------------------------------------------------------
histo = [0] * 10
for n in range(100000): val = randrange(0, 10); histo[val] += 1
pause("histogram of randrange(0,10) for 100000 values :\n%s" % histo)
# ------------------------------------------------------------------------------
# Take random values with uniform distribution on [0,1)
# ------------------------------------------------------------------------------
pause("random : %s" % [random() for n in range(10)])
# ------------------------------------------------------------------------------
# Histogram of the uniform distribution for 100000 random values
# ------------------------------------------------------------------------------
histo = [0] * 10
for n in range(100000): val = int(10*random()); histo[val] += 1
pause("histogram of random() for 100000 values :\n%s" % histo)
# ------------------------------------------------------------------------------
# Take random values with a gaussian distribution on R
# ------------------------------------------------------------------------------
pause("gauss(0,1) : %s" % [gauss(0,1) for n in range(10)])
# ------------------------------------------------------------------------------
# Histogram of the gaussian distribution for 1000000 random values
# ------------------------------------------------------------------------------
def clamp(val,a,b): return a if val < a else b if val > b else int(val) 
histo = [0] * 11
for n in range(100000): val = clamp(gauss(0,1),-5,5); histo[val+5] += 1
pause("histogram of gauss(0,1) for 100000 values :\n%s" % histo)
# ------------------------------------------------------------------------------
# Take random values with a gaussian distribution of mean=5 and variance=0.01
# ------------------------------------------------------------------------------
pause("gauss(5,0.01) : %s" % [gauss(5,.01) for n in range(10)])
# ------------------------------------------------------------------------------
# Histogram of the gaussian distribution for 1000000 random values
# ------------------------------------------------------------------------------
def clamp(val,a,b): return a if val < a else b if val > b else int(val) 
histo = [0] * 10
for n in range(100000): val = clamp(gauss(5,0.01),0,10); histo[val] += 1
pause("histogram gauss(5,0.01) for 100000 values :\n%s" % histo)
# ==============================================================================
