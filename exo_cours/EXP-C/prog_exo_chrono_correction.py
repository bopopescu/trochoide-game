# ==============================================================================
"""CHRONO : a user-controlled digital stopwatch"""
# ==============================================================================
__author__  = "Clément THION"
__version__ = "1.0"
__date__    = "2020-02-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def tick():
  """increment the counter and make recursive function call after 10ms"""
  win.chrono['text']+=1
  if win.start.state == 1: win.after(10, tick)
# ------------------------------------------------------------------------------
def on_start():
  """callback function for the 'START/STOP' button"""
  win.start.state=1-win.start.state
# ------------------------------------------------------------------------------
def on_reset():
  """callback function for the 'RESET' button"""
  win.chrono['text']=0
# ------------------------------------------------------------------------------
def main():
  """create the main window and pack the widgets"""
  global win
  font1, font2 = 'Arial 16', 'Times 120 bold'
  win = Win(title='CHRONO', font=font1, op=5)
  # ------------------------------------------------------------------------------
  frame = Frame(win, font=font1)
  win.start=Button(frame, text=('start', 'stop'), width=5, command=on_start)
  Button(frame, text="reset", command=on_reset)
  win.chrono = Label(win, text=0, font=font2, border=2)
  # ----------------------------------------------------------------------------
  win.loop()
# ------------------------------------------------------------------------------
if __name__ == '__main__':
  main()
# ==============================================================================