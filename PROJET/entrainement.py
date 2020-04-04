# ==============================================================================
"""THROCOÏDE"""
#un canva pour le cercle fix
#un canva pour le cercle mobil
#un canva pour la ligne sur le cercle mobil
#un canva pour la trochoïde (une suite de point, calculé dans Tick toute les 5ms, en changeant
#les coordonnées avec .Coords
#autre idée: create_polygone(ListeCoordonnées), en ajoutant via Tick un nvx point tt les 5ms,
# et en supprimant l'ancien polygone.
# ==============================================================================
__author__  = "Clément THION & Axel PLANTEY--VEUX"
__version__ = "1.0" # complex packing by using several levels of sub-frames
__date__    = "2019-03-28"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def tick():

def main():
    global win
    win = Win(title="trochoïde")
    win.canvas = Canvas(win, width=200, height=200, bg="blue")
    win.canvas.create_line(0,100,100,50)
    win.loop()

if __name__ == '__main__':
  main()