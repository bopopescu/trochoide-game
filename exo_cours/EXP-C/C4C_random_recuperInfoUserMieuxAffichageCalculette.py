# ==============================================================================
"""RANDOM : generate random values within a user-provided range"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "3.0" # store random values in a scrollable listbox
__date__    = "2018-01-15"
# ==============================================================================
from ezTK import *
from random import randrange
# ------------------------------------------------------------------------------
def on_entry():
  """callback function for the 'min,max' entry"""
  try: # try to parse the entry string as a couple of integer values
    minvalue, maxvalue = win.entry.state.split(',')
    minvalue, maxvalue = int(minvalue), int(maxvalue)
    win.min, win.max = min(minvalue, maxvalue), max(minvalue, maxvalue)
  except Exception:
    pass # keep previous values if the parsing fails
  win.entry.state = f"{win.min}, {win.max}"
# ------------------------------------------------------------------------------
def on_random():
  """callback function for the 'RANDOM' button"""
  on_entry() # reparse the entry string as user may forget to hit 'ENTER'
  minvalue, maxvalue, size = win.min, win.max, len(win.box)
  values = ["%2s" % randrange(minvalue,maxvalue+1) for loop in range(size+1)]
  win.box.append(' '.join(values)) # append new values as a single line
  #win.box(' '.join(values)) # replace box content with new values
# ----------------------------------------------------------------------------
def on_delete():
  """callback function for the 'DELETE' button"""
  del win.box[-1] # delete last line
  #del win.box[0:-1]  # delete all lines    
# ------------------------------------------------------------------------------
def main(minvalue=0, maxvalue=99):
  """create the main window and pack the widgets"""
  global win
  win = Win(title='RANDOM', op=5)
  # ----------------------------------------------------------------------------
  frame1 = Frame(win, border=1, op=5, grow=False)
  Label(frame1, text='Enter min,max :', grow=False)
  Entry(frame1, width=10, command=on_entry)
  frame2 = Frame(win, op=0, grow=False)
  Button(frame2, text='RANDOM', command=on_random)
  Button(frame2, text='DELETE', command=on_delete)
  Listbox(win, width=30, height=15, scroll=True, grow=True)
  # ----------------------------------------------------------------------------
  win.box, win.entry, win.min, win.max = win[2], frame1[1], minvalue, maxvalue
  on_entry(); win.loop()
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
