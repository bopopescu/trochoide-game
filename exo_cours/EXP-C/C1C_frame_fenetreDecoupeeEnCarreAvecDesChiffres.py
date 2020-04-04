# ==============================================================================
"""FRAME : demo program for the 'Win' and 'Frame' widgets"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "3.0" # 24 'Label' widgets with 2D packing
__date__    = "2018-01-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def main():
  """create the main window and pack the widgets"""
  global win
  # 2D packing is obtained by defining property 'fold' for window
  win = Win(title='FRAME', fold=6) # default 2D flow direction (= 'E' then 'S')
  #win = Win(title='FRAME', fold=3, flow='NE') # pack N then E, fold every 3
  #win = Win(title='FRAME', fold=12, flow='WN') # pack W then N, fold every 12
  # ----------------------------------------------------------------------------
  for loop in range(24):
    Label(win, text=loop, width=4, height=2, border=1)
  # ----------------------------------------------------------------------------
  properties(win)
  win.loop()
# ------------------------------------------------------------------------------
def properties(win):
  """view and edit some widget properties"""
  print("Number of widgets :", win.size) # get number of widgets as a tuple
  rows, cols = win.size # number of rows, number of cols
  for row in range(rows): # loop over widgets and get properties
    for col in range(cols):
      print("(%s,%s): text=%r" % (row, col, win[row][col]['text']))
  # ----------------------------------------------------------------------------
  win[2][1]['bg'] = 'red' # edit widget properties (use widget coordinates)
# ==============================================================================
if __name__ == "__main__":
  main()
# ==============================================================================
