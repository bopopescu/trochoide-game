# ==============================================================================
"""CANVAS : demo program for the Canvas widget"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "3.0" # create 6 moving sprites
__date__    = "2018-01-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def tick():
  """move all canvas items and make recursive function call after 10ms"""
  for item in win.items:
    xa, ya, xb, yb = win.canvas.bbox(item[0]) # get item coordinates
    vx, vy = item[1] # get item velocity
    xa, ya = xa + vx, ya + vy # edit item coordinates by adding velocity
    xb, yb = xb + vx, yb + vy
    if xa < -6 or xb > win.width+6:  vx = -vx # horizontal bounce (reverse vx)
    if ya < -6 or yb > win.height+6: vy = -vy # vertical bounce (reverse vy)
    win.canvas.coords(item[0], (xa+xb)//2, (ya+yb)//2) # update position
    item[1] = (vx, vy) # update velocity
  win.canvas.after(10, tick) # recursive call of 'tick' after 10ms
# ------------------------------------------------------------------------------
def main(width=640, height=480):
  """main program of the "canvas" module"""
  global win
  win = Win(title='CANVAS', grow=False)
  win.canvas = Canvas(win, width=width, height=height, bg='black')
  win.width, win.height, win.items = width, height, []
  # ----------------------------------------------------------------------------
  images = tuple(Image(file="smiley%s.png" % name) for name in '123456')
  for n in range(6): # create 6 image items (= sprites) on canvas
    dx, dy = width/7, height/7 # define position and velocity for each item
    x, y, vx, vy = dx + n*dx, dy + n*dy, 3-n, n-2
    win.items.append([win.canvas.create_image(x, y, image=images[n]), (vx, vy)])
  # ----------------------------------------------------------------------------
  win.after(1000, tick) # start animation after 1000ms
  win.loop()
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
