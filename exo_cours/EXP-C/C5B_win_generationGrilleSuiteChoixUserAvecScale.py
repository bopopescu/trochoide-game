# ==============================================================================
"""WIN : demo program for window manipulations"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "2.0" # dynamic creation and destruction of widgets 
__date__    = "2018-01-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def grid():
  """create the grid within the main window and pack the widgets"""
  del win[1] # delete the frame containing the current grid
  rows, cols = win.rowscale.state, win.colscale.state # get new grid size
  grid = Frame(win, fold=cols) # create a new frame to store the new grid
  colors = ('#F00','#0F0','#00F','#0FF','#F0F','#FF0')
  for loop in range(rows*cols):
    Brick(grid, height=50, width=50, bg=colors, state=loop)
# ------------------------------------------------------------------------------
def main(rows=9, cols=9):
  """create the main window and pack the widgets"""
  global win
  win = Win(title='CONFIG', op=2, grow=False)
  frame = Frame(win, fold=2)
  # ----------------------------------------------------------------------------
  Label(frame, text='Number of rows :', width=13, anchor='SW', grow=False)
  win.rowscale = Scale(frame, scale=(1,rows), flow='W', state=rows)
  Label(frame, text='Number of cols :', width=13, anchor='SW', grow=False)
  win.colscale = Scale(frame, scale=(1,cols), flow='W', state=cols)
  Button(frame, text='NEW GRID', command=grid)
  Frame(win) # create an empty frame to store the grid
  # ----------------------------------------------------------------------------
  win.loop()
# ==============================================================================
if __name__ == "__main__":
  main()
# ==============================================================================
