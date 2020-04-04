# ==============================================================================
"""TOGGLE : demo program for simple animation of multi-state widgets"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "5.0" # use Canvas for grid
__date__    = "2018-01-15"
# ==============================================================================
from ezTK import *
from random import randrange as rr
# ------------------------------------------------------------------------------
def tick():
  """update function for widget animation"""
  dim = win.dim; row, col = rr(dim), rr(dim) # select random position
  win.canvas.itemconfig(dim*row+col+1, image=win.images[rr(6)]) # set random state
  win.after(10, tick) # launch 'tick' again in 20 ms
# ------------------------------------------------------------------------------
def main(dim=12):
  """create the main window and pack the widgets"""
  global win # always define 'win' as a global variable
  win = Win(title='TOGGLE', bg='#000', op=2)
  # ----------------------------------------------------------------------------
  # store set of images used for grid cells
  win.images = tuple(Image(file="Z%s.gif" % color) for color in 'RGBCMY')
  width, height = win.images[0].width(), win.images[0].height()
  win.canvas = Canvas(win, width=dim*width, height=dim*height, bg='#FFF')
  for row in range(dim):
    for col in range(dim):
      win.canvas.create_image(row*height, col*width, anchor='nw',
        image=win.images[(row+col) % 6])
  # ----------------------------------------------------------------------------
  win.dim = dim; win.after(2000, tick); win.loop()
# ==============================================================================
if __name__ == "__main__":
  main()
# ==============================================================================
