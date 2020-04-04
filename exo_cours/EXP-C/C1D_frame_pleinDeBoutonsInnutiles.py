# ==============================================================================
"""FRAME : demo program for the 'Win' and 'Frame' widgets"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "4.0" # use sub-frames to get 2D packing
__date__    = "2018-01-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def main():
  """create the main window and pack the widgets"""
  font1, font2 = 'Arial 14', 'Arial 32 bold' # define fonts
  win = Win(title='FRAME', font=font1, op=2) # main window default flow='SE'
  # ----------------------------------------------------------------------------
  Button(win, text='OOOOOO', grow=False)
  # ----------------------------------------------------------------------------
  frame = Frame(win) # inner Frame with default flow='ES' (orthogonal flow)
  Button(frame, text='XXX\nXXX', grow=False)
  Button(frame, font=font2, text='YYY\nYYY') # use specific font
  Button(frame, text='ZZZ\nZZZ', grow=False)
  # ----------------------------------------------------------------------------
  Button(win, text='IIIIII', grow=False)
  # ----------------------------------------------------------------------------
  #properties(win, frame)
  win.loop()
# ------------------------------------------------------------------------------
def properties(win, frame):
  """view and edit some widget properties"""
  print("Number of widgets for win :", win.size)
  print("Number of widgets for frame :", frame.size)
  print("Text property for win[0] : %r" % win[0]['text']) 
  print("Text property for frame[0] : %r" % frame[0]['text']) 
  # ----------------------------------------------------------------------------
  frame[1]['text'] = '\u2660\u2663\u2665\u2666' # edit widget property
# ==============================================================================
if __name__ == "__main__":
  main()
# ==============================================================================
