# ==============================================================================
"""RANDOM : generate random values within a user-provided range"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "2.0" # use 'Entry' widget to define range
__date__    = "2018-01-15"
# ==============================================================================
from ezTK import *
from random import randrange as rr
# ------------------------------------------------------------------------------
def on_entry():
  """callback function for the 'min,max' entry"""
  try: # try to parse the entry string as a couple of integer values
    minvalue, maxvalue = win.entry.state.split(',') #check if separation
    minvalue, maxvalue = int(minvalue), int(maxvalue) #check if int
    win.min, win.max = min(minvalue, maxvalue), max(minvalue, maxvalue) #reorder 
  except Exception:
    pass # keep previous values if the parsing fails
  win.entry.state = "%s, %s" % (win.min, win.max)
# ------------------------------------------------------------------------------
def on_random():
  """callback function for the 'RANDOM' button"""
  on_entry() # reparse the entry string as user may forget to hit 'ENTER'
  win.label['text'] = rr(win.min, win.max+1)
# ------------------------------------------------------------------------------
def main(minvalue=0, maxvalue=99):
  """create the main window and pack the widgets"""
  global win
  win = Win(title='RANDOM', op=5)
  # ----------------------------------------------------------------------------
  frame = Frame(win, border=1, op=5, grow=False)
  Label(frame, text='Enter min,max :', grow=False)
  Entry(frame, width=10, command=on_entry)
  Button(win, text='RANDOM', command=on_random, grow=False)
  Label(win, font='Arial 72 bold', width=3, border=1)
  # ----------------------------------------------------------------------------
  win.label, win.entry, win.min, win.max = win[2], frame[1], minvalue, maxvalue
  on_entry(); win.loop()
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
