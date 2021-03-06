# ==============================================================================
"""FRAME : demo program for the 'Win' and 'Frame' widgets"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "1.0" # one single 'Brick' widget
__date__    = "2018-01-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def main():
  """create the main window and pack the widgets"""
  win = Win(title='TOTO') # create main window
  Brick(win, width=300, height=200, bg='blue') # create Brick widget
  win.loop() # start event loop  
# ==============================================================================
if __name__ == "__main__":
  main()
# ==============================================================================

#propriété = une donné qui va caractériser une des données visuelle de la fenêtre.