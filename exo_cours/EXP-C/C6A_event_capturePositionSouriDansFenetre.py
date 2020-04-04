# ==============================================================================
"""EVENT : demo program for keyboard and mouse event handlers"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "1.0" # check mouse events (move)
__date__    = "2018-01-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def on_move(widget, code, mods):
  """callback function for all 'mouse move' events"""
  # display event parameters, only when 'win.brick' is the active widget
  if widget == win.brick: display('move', code, mods)
# ------------------------------------------------------------------------------
def display(event, code, mods):
  """display event parameters"""
  win.label['text'] = "Event = %r  Code = %r  Mods = %r" % (event, code, mods)
# ------------------------------------------------------------------------------
def main():
  """create the main window and pack the widgets"""
  global win
  win = Win(title='EVENT', move=on_move, op=2, grow=False)
  Label(win, font='Arial 14', height=2, border=2)
  Brick(win, width=640, height=480, bg='#00F')
  # ----------------------------------------------------------------------------
  win.label, win.brick = win[0], win[1]; win.loop()
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
