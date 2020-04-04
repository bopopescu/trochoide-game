# ==============================================================================
"""TOGGLE : demo program for simple animation of multi-state widgets"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "4.0" # combine several properties in multi-state widgets
__date__    = "2018-01-15"
# ==============================================================================
from ezTK import *
from random import randrange as rr
# ------------------------------------------------------------------------------
def tick():
  """update function for widget animation"""
  rows, cols = win.size # get grid size
  states = win[0][0].states # get total number of states for grid cells
  row, col = rr(rows), rr(cols) # select random position
  win[row][col].state = rr(states) # set random widget to random state
  win.after(20, tick) # launch 'tick' again in 20 ms
# ------------------------------------------------------------------------------
def main(rows=5, cols=8):
  """create the main window and pack the widgets"""
  global win # always define 'win' as a global variable
  bg = ('#F00','#0F0','#00F','#0FF','#F0F','#FF0','#000','#FFF')
  fg = ('#FFF','#000') # number of states may be different for each property
  text = ('RED','GREEN','BLUE','CYAN','MAGENTA','YELLOW','BLACK','WHITE')
  win = Win(title='TOGGLE', font='Arial 16 bold', fold=cols, op=2)
  # ----------------------------------------------------------------------------
  for loop in range(rows*cols): # loop over grid cells
    Label(win, height=3, width=9, text=text, bg=bg, fg=fg, state=loop)
  # ----------------------------------------------------------------------------
  win.after(2000, tick); win.loop()
# ==============================================================================
if __name__ == "__main__":
  main()
# ==============================================================================
