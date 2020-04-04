# ==============================================================================
"""TXTFILE : demo for 'read_txt/write_txt' functions from the 'ezCLI' toolbox"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "1.0"
__date__    = "2015-07-01"
__usage__   = """
Simply press <ENTER> at each pause""" 
# ==============================================================================
from ezCLI import *
# ------------------------------------------------------------------------------
# Sample use cases for 'read_txt'
# ------------------------------------------------------------------------------
# read the whole content from file
txt = read_txt('test-txt.txt')
pause(">>> read all lines :\n%s" % txt)

# return line at index 4 from file
txt = read_txt('test-txt.txt', 4)
pause(">>> read line at index 4 :\n%s" % txt)

# return lines in range(4,7) from file
txt = read_txt('test-txt.txt', 4, 7)
pause(">>> read lines in range(4,7) :\n%s" % txt)

# return the first 3 lines from file
txt = read_txt('test-txt.txt', None, 3)
pause(">>> read the first 3 lines :\n%s" % txt)

# return the last 5 lines from file
txt = read_txt('test-txt.txt', -5, None)
pause(">>> read the last 5 lines :\n%s" % txt)

# ------------------------------------------------------------------------------
# Sample use cases for 'write_txt'
# ------------------------------------------------------------------------------
# replace the whole file and return the new file content
txt = write_txt('test.txt', 'ccc\nccc\nccc')
pause(">>> replace whole content :\n%s" % txt)

# insert line at index 2 and return new file content
txt = write_txt('test.txt', 'ddd', 2)
pause(">>> insert line at index 2 :\n%s" % txt)

# insert line at end of file and return new file content
txt = write_txt('test.txt', 'eee', -1)
pause(">>> insert line at end of file :\n%s" % txt)

# replace first line and return new file content
txt = write_txt('test.txt', 'aaa\nbbb', None, 1)
pause(">>> replace the first line :\n%s" % txt)

# replace the last 2 lines and return new file content
txt = write_txt('test.txt', 'eee\nfff\nggg', -2, None)
pause(">>> replace the last 2 lines :\n%s" % txt)
# ==============================================================================
