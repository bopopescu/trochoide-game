# ==============================================================================
"""CANVAS : demo program for the Canvas widget"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "1.0" # draw lines, rectangles, ovals, strings and images
__date__    = "2018-01-15"
# ==============================================================================
from ezTK import *
from random import randrange as rr
# ------------------------------------------------------------------------------
def draw_rect():
  """draw a set of color rectangles"""
  steps, colors = 20, ('#F00','#0F0','#00F','#FF0','#000')
  w, h = win.width, win.height; dw, dh = w/steps/2, h/steps/2
  for n in range(steps):
    win.canvas.create_rectangle(n*dw, n*dh, w-n*dw, h-n*dh, width=3,
      outline=colors[4], fill=colors[n%4]) 
# ------------------------------------------------------------------------------
def draw_oval():
  """draw a set of color ovals"""
  steps, colors = 20, ('#F00','#0F0','#00F','#FF0','#000')
  w, h = win.width, win.height; dw, dh = w/steps/2, h/steps/2
  for n in range(steps):
    win.canvas.create_oval(n*dw, n*dh, w-n*dw, h-n*dh, width=3,
      outline=colors[4], fill=colors[n%4]) 
# ------------------------------------------------------------------------------
def draw_line():
  """draw a set of color lines"""
  steps, colors = 20, ('#F00','#0F0','#00F','#FF0')
  w, h = win.width, win.height; dw, dh = w/steps, h/steps
  for n in range(steps):
    win.canvas.create_line(n*dw, 0, w,   n*dh, width=2, fill=colors[0]) 
    win.canvas.create_line(n*dw, 0, 0, h-n*dh, width=2, fill=colors[1]) 
    win.canvas.create_line(n*dw, h, 0,   n*dh, width=2, fill=colors[2]) 
    win.canvas.create_line(n*dw, h, w, h-n*dh, width=2, fill=colors[3]) 
# ------------------------------------------------------------------------------
def draw_curve():
  """draw a set of curves by sampling mathematical functions"""
  from math import cos, exp
  w, h, colors = win.width//2, win.height//2, ('#000','#0F0','#F00','#00F')
  for n in range(4): # loop over curves
    xa, ya, xb, yb = 0, h, 0, h # initial position for each curve
    for x in range(w+1): # loop over horizontal axis
      t = 2*x/w - 1 # parameter t moves over range [-1,1]
      if n == 0: xa, ya, xb, yb = xb, yb, 2*x, h
      elif n == 1: xa, ya, xb, yb = xb, yb, 2*x, h - h*exp(-5*t*t)
      elif n == 2: xa, ya, xb, yb = xb, yb, 2*x, h + h*exp(-5*t*t)
      else: xa, ya, xb, yb = xb, yb, 2*x, h + h*exp(-5*t*t)*cos(25*t)
      win.canvas.create_line(xa, ya, xb, yb, width=2, fill=colors[n])  
# ------------------------------------------------------------------------------
def draw_text():
  """draw a set of strings in a grid"""
  steps, colors, font = 12, ('#F00','#0F0','#00F','#000'), 'Arial 12 bold'
  w, h = win.width, win.height; dw, dh = w/steps, h/steps
  for row in range(steps):
    for col in range(steps):
      x, y, n = dw/2 + dw*col, dh/2 + dh*row, (col+1)*(row+1)
      win.canvas.create_text((x,y), text=n, font=font, fill=colors[(col+row)%3])
  # ----------------------------------------------------------------------------
  for n in range(1, steps):
    win.canvas.create_line(0, n*dh, w, n*dh, width=2, fill=colors[3]) 
    win.canvas.create_line(n*dw, 0, n*dw, h, width=2, fill=colors[3]) 
# ------------------------------------------------------------------------------
def draw_image():
  """draw a set of images at random position"""
  x, y, n = rr(win.width), rr(win.height), rr(len(win.images))
  win.canvas.create_image(x, y, image=win.images[n])
  win.after(20, draw_image) # recursive call of 'draw_image' after 20ms
# ------------------------------------------------------------------------------
def wait():
  """wait for user click, then clear canvas"""
  MessageDialog.showinfo('', message='Click to draw new shape')
  win.canvas.delete('all')
# ------------------------------------------------------------------------------
def main(width=480, height=480):
  """main program of the "canvas" module"""
  global win
  win = Win(title='CANVAS', grow=False)
  win.canvas = Canvas(win, width=width, height=height)
  win.images = [Image(file="smiley%s.png" % name) for name in '123456']
  win.width, win.height = width, height
  # ----------------------------------------------------------------------------
  draw_rect(); wait(); draw_oval(); wait(); draw_line(); wait()
  draw_curve(); wait(); draw_text(); wait(); draw_image(); win.loop()
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
