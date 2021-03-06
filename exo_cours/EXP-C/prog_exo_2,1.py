# ==============================================================================
"""FRAME : demo program for the 'Win' and 'Frame' widgets"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "7.0" # add callback function with 'command' option 
__date__    = "2018-01-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def main():
  """create the main window and pack the widgets"""
  font1, font2 = 'Arial 14', 'Arial 48 bold'
  win = Win(title='FRAME', font=font1, op=2)
  # ----------------------------------------------------------------------------
  fr1 = Frame(win, grow=False)
  Button(fr1, text='IIIIII')
  Button(fr1, text='XXX\nXXX', grow=False)
  Button(fr1, text='IIIIII')
  # ----------------------------------------------------------------------------
  fr2 = Frame(win)
  fr3 = Frame(fr2, grow=False)
  Button(fr3, text='OOOOOO', grow=False)
  Button(fr3, text='XXX\nXXX')
  Button(fr3, text='OOOOOO', grow=False)
  fr3_1 = Frame(fr2, grow=True, fold=2, flow="ES")
  Button(fr3_1, text='E', command=win.exit, bg="red")
  Button(fr3_1, text='X', command=win.exit, bg="red")
  Button(fr3_1, text='I', command=win.exit, bg="red")
  Button(fr3_1, text='T', command=win.exit, bg="red")
  #Button(fr2, text='EXIT', font=font2, fg='#FFF', bg='#00F', command=win.exit)
  Button(fr2, text='OOOOOO', grow=False)
  # ----------------------------------------------------------------------------
  fr4 = Frame(win, grow=False)
  Button(fr4, text='XXX\nXXX', grow=False)
  Button(fr4, text='IIIIII')
  Button(fr4, text='XXX\nXXX', grow=False)
  # ----------------------------------------------------------------------------
  win.loop()
# ==============================================================================
if __name__ == "__main__":
  main()
# ==============================================================================