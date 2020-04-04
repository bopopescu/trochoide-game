# ==============================================================================
"""GRID : create some grids with several color or black/white patterns"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "0.0" # skeleton version
__date__    = "2018-01-15"
Color=["red", "green", "blue", "lightblue", "black", "lightgreen"]
ColorS = ["black", "white"]
Suite = [13+1, 13-2, 2, 1, 13-4, 1, 2, 1, 2, 1, 1,  ]
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# faire une fonction qui fait les trois brick en 1 de large
#à gauche et à droite)
#
        

def boxes(width=400, height=400, cols=13, rows=13):
    win = Win(fold=13)
    for row in range(rows):
        for col in range (cols):
            

    win.loop()

    






# ------------------------------------------------------------------------------
def colorboxes(width=400, height=400, rows=13, cols=13):
  """create concentric color boxes"""
# ==============================================================================
if __name__ == "__main__":

  #stripes()
  #chessboard()
  #colorboard()
  boxes()
  #colorboxes()
# ==============================================================================