# ==============================================================================
"""TOGGLE : demo program for simple animation of multi-state widgets"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "2.0" # use multi-state widgets for animation
__date__    = "2018-01-15"
# ==============================================================================
from ezTK import *
from random import randrange as rr
# ------------------------------------------------------------------------------
def tick():
  """update function for widget animation"""
  rows, cols = win.size # get number of rows and number of cols
  states = win[0][0].states # get number of states
  row, col = rr(rows), rr(cols) # select random position
  win[row][col].state = rr(states) # set selected widget to random state
  win.after(20, tick) # launch 'tick' again in 20 ms
# ------------------------------------------------------------------------------
def main():
  """create the main window and pack the widgets"""
  global win # always define 'win' as a global variable
  win = Win(title='TOGGLE', fold=5, border=1) # fold every 5 widgets
  # ----------------------------------------------------------------------------
  colors = ('#F00','#0F0','#00F','#0FF','#F0F','#FF0') # define color set
  for loop in range(25): # loop over grid cells (5x5)
    Brick(win, height=64, width=64, bg=colors, state=2) # multi-state 'Brick'
  # ----------------------------------------------------------------------------
  win.after(2000, tick); win.loop()
# ==============================================================================
if __name__ == "__main__":
  main()
# ==============================================================================
