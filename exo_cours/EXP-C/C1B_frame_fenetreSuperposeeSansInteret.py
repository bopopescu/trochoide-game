# ==============================================================================
"""FRAME : demo program for the 'Win' and 'Frame' widgets"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "2.0" # 3 'Brick' widgets with 1D packing
__date__    = "2018-01-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def main():
  """create the main window and pack the widgets"""
  global win # always define 'win' as a global variable
  #win = Win(title='FRAME') # use default 1D flow direction (= 'S')
  #win = Win(title='FRAME', flow='W') # change flow direction (= 'E','N' or 'W')
  win = Win(title='FRAME', op=5) # add outer padding (in pixel units)
  # ----------------------------------------------------------------------------
  A, B, C = 'red', 'lime', 'blue'
  #A, B, C = '#FF0000', '#00FF00', '#0000FF'
  #A, B, C = '#F00', '#0F0', '#00F'
  Brick(win, width=150, height=100, bg=A)
  Brick(win, width=150, height=100, bg=B)
  Brick(win, width=150, height=100, bg=C)
  # ----------------------------------------------------------------------------
  properties()
  win.loop()
# ------------------------------------------------------------------------------
def properties():
  """view and edit some widget properties"""
  print("Number of widgets :", win.size) # get number of widgets used in 'win'
  for n in range(win.size): # loop over widgets and get their properties
    bg, width, height = win[n]['bg'], win[n]['width'], win[n]['height']; 
    print("* Properties for win[%s] :" % n)
    print("  bg=%s width=%s height=%s" % (bg, width, height))
  # ----------------------------------------------------------------------------
  win[0]['bg'] = 'white' # edit widget property (use widget index)
# ==============================================================================
if __name__ == "__main__":
  main()
# ==============================================================================
