# ==============================================================================
"""EVENT : demo program for keyboard and mouse event handlers"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "2.0" # check mouse events (inout and click)
__date__    = "2018-01-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def on_click(widget, code, mods):
  """callback function for all 'mouse click' events"""
  if widget.main != win.grid or widget.index is None:
    return # nothing to do if the widget is not a grid cell 
  display('click', widget.index, code, mods)
  if 'Alt' in mods: reset() # reset grid state for any mouse click + 'ALT' key
  elif code == 'LMB': widget.state += 1 # increment state for left click
  elif code == 'RMB': widget.state -= 1 # decrement state for right click
  elif code == 'MMB': reset() # reset grid state for middle click
# ------------------------------------------------------------------------------
def on_inout(widget, code, mods):
  """callback function for all 'mouse in' or 'mouse out' events"""
  if widget.main != win.grid or widget.index is None:
    return # nothing to do if the widget is not a grid cell
  display('inout', widget.index, code, mods)
  if code: widget['bg'] = '#FFF' # code = 1 for mouse in --> white background
  else: widget.state += 0 # code = 0 for mouse out --> restore background
# ------------------------------------------------------------------------------
def reset():
  """reset initial windows state"""
  win.label['text'] = '' # clear label widget
  rows, cols = win.grid.size
  for loop in range(rows*cols): # loop over grid cells
    row, col = loop // cols, loop % cols # get coordinates by Euclidian division
    win.grid[row][col].state = 0 # reset each cell
# ------------------------------------------------------------------------------
def display(event, index, code, mods):
  """display event parameters"""
  win.label['text'] = ("Event = %r  Index = %r  Code = %r  Mods = %r" %
    (event, index, code, mods))
# ------------------------------------------------------------------------------
def main(rows=3, cols=12):
  """create the main window and pack the widgets"""
  global win
  colors = ('#00F','#0F0','#F00','#0FF','#F0F','#FF0')
  win = Win(title='EVENT', click=on_click, inout=on_inout, op=2, grow=False)
  Label(win, font='Arial 14', height=2, border=2)
  grid = Frame(win, fold=cols)
  for loop in range(rows*cols):
    Brick(grid, height=64, width=64, bg=colors)
  # ----------------------------------------------------------------------------
  win.label, win.grid = win[0], win[1]; win.loop()
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
