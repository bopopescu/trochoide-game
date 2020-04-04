# ==============================================================================
"""GRID : create some grids with several color or black/white patterns"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "0.0" # skeleton version
__date__    = "2018-01-15"
Color=["red", "green", "blue", "lightblue", "black", "lightgreen"]
ColorS = ["black", "white"]
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def chessboard(width=400, height=400, cols=8, rows=8):
  """create black and white chessboard"""
  win = Win(title="chessboard", fold=8)

  #l'alternance blanc noir de collone se fait avec first_collor, celle de ligne se fait avec loop
  for first_color in range(rows): #lignes            8*8 cases, each case = one brick
    for loop in range(rows): #collones
      Brick(win, width=width//cols, height=height//rows, border=0, bg=ColorS[(first_color+loop)%len(ColorS)])
  win.loop()


# ------------------------------------------------------------------------------
def colorboard(width=400, height=400, cols=8, rows=8):
  """create six color checkerboard"""
  win = Win(title="colorboard", fold=8, op=5)
  #même principe que pour chessboard
  for first_color in range(8): #lignes            8*8 cases, each case = one brick
    for loop in range(8): #collones
      Brick(win, width=width//8, height=height//8, border=0, bg=Color[(first_color+loop)%len(Color)])
  win.loop()
# ------------------------------------------------------------------------------
def boxes(width=400, height=400, cols=13, rows=13):
  """create concentric black and white boxes"""
# ------------------------------------------------------------------------------
def colorboxes(width=400, height=400, rows=13, cols=13):
  """create concentric color boxes"""
# ==============================================================================
if __name__ == "__main__":

  #colorstripes()
  #chessboard()
  colorboard()
  #boxes()
  #colorboxes()
# ==============================================================================