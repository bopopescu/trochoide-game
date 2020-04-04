# ==============================================================================
"""CSVFILE : demo for 'read_csv/write_csv' functions from the 'ezCLI' toolbox"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "1.0"
__date__    = "2015-07-01"
__usage__   = """
Simply press <ENTER> at each pause""" 
# ==============================================================================
from ezCLI import *
# ------------------------------------------------------------------------------
# Sample use cases for 'read_csv'
# ------------------------------------------------------------------------------
# first read the file as a text file to show its raw content
txt = read_txt('test-csv.txt')
pause(">>> read CSV file as a TXT file :\n%s" % txt)

# return the matrix stored in file and apply 'convert' to all cells
csv = read_csv('test-csv.txt')
pause(">>> read CSV file as a matrix :\n%s" % csv)

# return the matrix stored in file but keep all cells as strings
csv = read_csv('test-csv.txt', raw=True)
pause(">>> read CSV file as a matrix of strings :\n%s" % csv)

# ------------------------------------------------------------------------------
# Sample use cases for 'write_csv'
# ------------------------------------------------------------------------------
# create a sample non-rectangular 3D matrix containing 16 different cells
mat = [[list('abcde'), 'aa,bb,cc', ('dd','ee')], [1,(2,3),[4,5,6]]]
pause(">>> create a sample 3D matrix :\n%s" % mat)

# replace the whole file and return the new file content
csv = write_csv('test.txt', mat)
pause(">>> write matrix as a CSV file:\n%s" % csv)

# insert new block at head and return new file content
csv = write_csv('test.txt', '1,2,3\n4,5,6', 0)
pause(">>> insert new block at head:\n%s" % csv)

# insert new block at tail and return new file content
csv = write_csv('test.txt', [7,8,9], -1)
pause(">>> insert new block at tail:\n%s" % csv)

# replace the first two blocks and return new file content
csv = write_csv('test.txt', mat[1], None, 2)
pause(">>> replace the first two blocks:\n%s" % csv)

# replace the last two blocks and return new file content
csv = write_csv('test.txt', mat[0], -2, None)
pause(">>> replace the last two blocks:\n%s" % csv)
# ==============================================================================
