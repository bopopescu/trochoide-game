# ==============================================================================
"""RANDOM : generate random values within a user-provided range"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "1.0" # use a Label widget to display single random value
__date__    = "2018-01-15"
# ==============================================================================
from ezTK import *
from random import randrange as rr
# ------------------------------------------------------------------------------
def on_scale(flag):
  """callback function for the 'MIN' and 'MAX' scales"""
  # get value of active scale, according to flag
  active = (win.minscale.state, win.maxscale.state)[flag]
  win.minscale.state = min(win.minscale.state, active)
  win.maxscale.state = max(win.maxscale.state, active)
# ------------------------------------------------------------------------------
def on_random():
  """callback function for the 'RANDOM' button"""
  win.label['text'] = rr(win.minscale.state, win.maxscale.state+1)
# ------------------------------------------------------------------------------
def main(minvalue=0, maxvalue=999):
  """create the main window and pack the widgets"""
  global win
  win = Win(title='RANDOM', op=5)
  # ----------------------------------------------------------------------------
  frame = Frame(win, op=0, grow=False)
  Label(frame, text='MIN :', anchor='SE', grow=False)
  Scale(frame, scale=(minvalue, maxvalue), state=minvalue,
        command=lambda: on_scale(0)) # flag = 0
  Label(frame, text='MAX :', anchor='SE', grow=False)
  Scale(frame, scale=(minvalue, maxvalue), state=maxvalue,
        command=lambda: on_scale(1)) # flag = 1
  Button(win, text='RANDOM', command=on_random, grow=False)
  Label(win, font='Arial 72 bold', width=3, border=2)
  # ----------------------------------------------------------------------------
  # set friendly names for all widgets used in callbacks
  win.label, win.minscale, win.maxscale = win[2], frame[1], frame[3]; win.loop()
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
