# ==============================================================================
"""GRID : create some grids with several color or black/white patterns"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "0.0" # skeleton version
__date__    = "2018-01-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
Color=["red", "green", "blue", "lightblue", "black", "lightgreen"]
def stripes(width=500, height=800, rows=40):
  """alternate black and white horizontal stripes"""
  win = Win(fold=1)
  for loop in range(rows):
      Brick(win, width=width, height=(height//rows), border=0, bg=Color[loop%len(Color)])
  win.loop()
# ------------------------------------------------------------------------------
def colorstripes(width=400, height=400, rows=40):
  """alternate color stripes using six colors"""
# ------------------------------------------------------------------------------
def chessboard(width=400, height=400, cols=8, rows=8):
  """create black and white chessboard"""
# ------------------------------------------------------------------------------
def colorboard(width=400, height=400, cols=8, rows=8):
  """create six color checkerboard"""
# ------------------------------------------------------------------------------
def boxes(width=400, height=400, cols=13, rows=13):
  """create concentric black and white boxes"""
# ------------------------------------------------------------------------------
def colorboxes(width=400, height=400, rows=13, cols=13):
  """create concentric color boxes"""
# ==============================================================================
if __name__ == "__main__":
  stripes()
  #colorstripes()
  #chessboard()
  #colorboard()
  #boxes()
  #colorboxes()
# ==============================================================================