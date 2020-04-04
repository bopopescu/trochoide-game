# ==============================================================================
"""INIFILE : demo for 'read_ini/write_ini' functions from the 'ezCLI' toolbox"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "1.0"
__date__    = "2015-07-01"
__usage__   = """
Simply press <ENTER> at each pause""" 
# ==============================================================================
from ezCLI import *
# ------------------------------------------------------------------------------
# Sample use cases for 'read_ini'
# ------------------------------------------------------------------------------
# first read the file as a text file to show its raw content
txt = read_txt('test-ini.txt')
pause(">>> read INI file as a TXT file :\n%s" % txt)

# return the data stored in file and apply 'convert' to all items
ini = read_ini('test-ini.txt')
pause(">>> read INI file and convert all data type :\n%s" % ini)

# return the data stored in file but keep all items as strings
ini = read_ini('test-ini.txt', raw=True)
pause(">>> read INI file as keep all data as strings :\n%s" % ini)

# ------------------------------------------------------------------------------
# Sample use cases for 'write_ini'
# ------------------------------------------------------------------------------
# sample data containing 5 properties spread in 3 sections  
items = {'':{'a':1,'b':2},'AAA':{'aa':1.2,'bb':''},'BBB':{'cc':'#'}}
pause(">>> sample structured data : \n%s" % items)

# replace the whole file and return the new file content
ini = write_ini('test.txt', items)
pause(">>> write structured data as an INI file : \n%s" % ini)

# insert new section at tail and return new file content
ini = write_ini('test.txt', '\n[CCC]\nzz = 0', -1)
pause(">>> insert new section at tail : \n%s" % ini)

# replace property stored at line 4 and return new file content
ini = write_ini('test.txt', {'aa':2.5}, 4, 5)
pause(">>> replace property stored at line 4 : \n%s" % ini)
# ==============================================================================
