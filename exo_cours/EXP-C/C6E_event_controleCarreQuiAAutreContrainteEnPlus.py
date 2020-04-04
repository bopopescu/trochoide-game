# ==============================================================================
"""EVENT : demo program for key press and mouse click event handlers"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "5.0" # combine time events and user events
__date__    = "2018-01-15"
# ==============================================================================
from ezTK import *
from random import choice
# ------------------------------------------------------------------------------
def move(code):
  """move the green square according to 'code'"""
  moves = {'Up':(1,0), 'Down':(-1,0), 'Right':(0,1), 'Left':(0,-1)}
  # compute new cursor position by using modulo to get automatic cycling
  rows, cols = win.size # get grid size
  row, col = win.cursor.index # get current position for cursor
  row_move, col_move = moves[code] # get vertical and horizontal move
  # compute new position for cursor by using modulo to get automatic cycling
  row, col = (row + row_move) % rows, (col + col_move) % cols
  if win[row][col].state == 2: return # cursor blocked by red square
  win.cursor.state = 0; win.cursor = win[row][col]; win.cursor.state = 1 # move
# ------------------------------------------------------------------------------
def tick():
  """time-controlled window update"""
  move(choice(('Up','Down','Right','Left'))) # pick a random direction
  win.after(500, tick)
# ------------------------------------------------------------------------------
def on_key(widget, code, mods):
  """callback function for each key press in the window"""
  if code not in ('Up','Down','Right','Left'): return # key is not an arrow key
  move(code)
# ------------------------------------------------------------------------------
def main(rows=9, cols=9, size=64):
  """create the main window and pack the widgets"""
  global win
  win = Win(title='EVENT', flow='EN', fold=cols, key=on_key, grow=False)
  colors = ('#00F','#0F0','#F00') # define color set for board cells
  # ----------------------------------------------------------------------------
  for loop in range(rows*cols):
    Brick(win, bg=colors, height=size, width=size)
  # ---------------------------------------------------------------------------
  # put cursor (= green cell) at the center of the grid
  win.cursor = win[rows//2][cols//2]; win.cursor.state = 1
  # put some walls (= red cells) near the corners of the grid
  walls = ((0,0),(1,0),(0,1),(-1,-1),(-2,-1),(-1,-2),(-1,0),(0,-1))
  for row,col in walls: win[row][col].state = 2
  # ----------------------------------------------------------------------------
  win.after(1000, tick); win.loop()
# ==============================================================================
if __name__ == '__main__':
  main() # create window with default parameters
  #main(32,32,20)
# ==============================================================================
