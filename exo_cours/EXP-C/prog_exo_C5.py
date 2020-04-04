# ==============================================================================
"""LEAP FROG : implement the LeapFrog puzzle"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "0.0" # skeleton for both mouse-based and keyboard-based versions
__date__    = "2019-03-01"
# ------------------------------------------------------------------------------
from ezTK import *
# ------------------------------------------------------------------------------
def on_reset():
  """callback function for the 'RESET' button"""
  # TODO
# ------------------------------------------------------------------------------
def on_click(widget, code, mods):
  """callback function for all keyboard events"""
  print(widget, code, mods)
  # TODO
# ------------------------------------------------------------------------------
def on_key(widget, code, mods):
  """callback function for all keyboard events"""
  print(widget, code, mods)
  # TODO
# ------------------------------------------------------------------------------
def main(frog=3):
  """create the main window and pack the widgets"""
  global win
  win = Win(title='LEAP FROG', op=3, click=on_click) # mouse-based
  #win = Win(title='LEAP FROG', op=3, key=on_key) # keyboard-based
  # TODO
  on_reset(); win.loop() # set initial configuration and start event loop
# ------------------------------------------------------------------------------
if __name__ == '__main__':
  main() # create window with default game parameters: frog=3
  #main(7) # try with 7 frogs per color
# ==============================================================================