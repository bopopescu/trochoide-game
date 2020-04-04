# ==============================================================================
"""REPLACE : replace all occurrences of a string in a given text file"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "1.0" # process a single file
__date__    = "2015-09-01"
__usage__   = """
User input : <oldstring> <newstring> <filename> 
App output : modify 'filename' by replacing each 'oldstring' by 'newstring'
Note: use quotes if 'oldstring' or 'newstring' contains space characters"""
# ==============================================================================
from ezCLI import *
# ------------------------------------------------------------------------------
def replace(oldstring, newstring, name):
  """replace each occurrence of 'oldstr' by 'newstr' in file 'name'"""
  text = read_txt(name) # read whole content of file 'name'
  count = text.count(oldstring); #inspect()
  text = text.replace(oldstring, newstring); #inspect()
  write_txt(name, text) # write whole content of file 'name'
  return "%s : %s strings have been replaced" % (name, count)
# ------------------------------------------------------------------------------
def parser(command):
  """extract arguments from 'command' before calling 'replace()'"""
  oldstring, newstring, name = parse(command); #inspect()
  return replace(oldstring, newstring, name)
# ==============================================================================
if __name__ == '__main__':
  userloop(parser, "Enter <oldstr> <newstr> <name>")
# ==============================================================================
