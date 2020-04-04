# ==============================================================================
"""CANVAS : demo program for the Canvas widget"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "2.0" # create 3 moving circles
__date__    = "2018-01-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def tick():
  """move all canvas items and make recursive function call after 10ms"""
  for item in win.items:
    xa, ya, xb, yb = win.canvas.coords(item[0]) # get item coordinates
    vx, vy = item[1] # get item velocity
    xa, ya = xa + vx, ya + vy # edit item coordinates by adding velocity
    xb, yb = xb + vx, yb + vy
    if xa < 0 or xb > win.width:  vx = -vx # horizontal bounce (reverse vx)
    if ya < 0 or yb > win.height: vy = -vy # vertical bounce (reverse vy)
    win.canvas.coords(item[0], xa, ya, xb, yb) # update position
    item[1] = (vx, vy) # update velocity
  win.canvas.after(10, tick) # recursive call of 'tick' after 10ms
# ------------------------------------------------------------------------------
def main(width=640, height=480):
  """main program of the "canvas" module"""
  global win
  win = Win(title='CANVAS', grow=False)
  win.canvas = Canvas(win, width=width, height=height)
  win.width, win.height, win.items = width, height, []
  # ----------------------------------------------------------------------------
  colors = ('#F00','#0F0','#00F','#000')
  for n in range(3): # create 3 oval items on canvas
    # define dimension, position and velocity for each item
    dim, dx, dy = min(width,height)/8, width/4, height/4
    x, y, vx, vy = dx + n*dx, dy + n*dy, 3-n, n+1
    win.items.append([win.canvas.create_oval(x-dim, y-dim, x+dim, y+dim,
      width=5, outline=colors[3], fill=colors[n]), (vx, vy)])
  # ----------------------------------------------------------------------------
  win.after(1000, tick) # start animation after 1000ms
  win.loop()
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
