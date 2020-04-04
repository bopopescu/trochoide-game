# ==============================================================================
"""TOGGLE : demo program for simple animation of multi-state widgets"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "3.0" # use image Labels for grid cells
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
  win = Win(title='TOGGLE', bg='#000', fold=5, op=2) # fold every 5 widgets
  # ----------------------------------------------------------------------------
  # store set of images used for grid cells
  image = tuple(Image(file="Z%s.gif" % color) for color in 'RGBCMY')
  # alternative version without list comprehension:
  #image = (Image(file='ZR.gif'), Image(file='ZG.gif'),
  #         Image(file='ZB.gif'), Image(file='ZC.gif'),
  #         Image(file='ZM.gif'), Image(file='ZY.gif'))
  for loop in range(25): # loop over grid cells (5x5)
    Label(win, image=image, state=loop) # use different states for grid cells
  # ----------------------------------------------------------------------------
  win.after(2000, tick); win.loop()
# ==============================================================================
if __name__ == "__main__":
  main()
# ==============================================================================
