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
  if win.startButton['text']=='start':
      win.label['text']+=1 #increment one centiem of second
      win.after(100, tick)
  else:
      win.startButton['text']=='stop'
# ------------------------------------------------------------------------------
def on_start():
  """callback function for the 'START/STOP' button"""
  if win.startButton['text']=='start':  #if we've pushed "start"
      win.startButton['text']='stop'
  else: #if we've pushed "stop"
      win.startButton['text']='start'
# ------------------------------------------------------------------------------
def on_reset():
  """callback function for the 'RESET' button"""
  win.label['text']=0
# ------------------------------------------------------------------------------
def main():
  """create the main window and pack the widgets"""
  global win
  font1, font2 = 'Arial 16', 'Times 120 bold'

  win = Win(title='CHRONO', font=font1, op=5)
  frame1 = Frame(win)
  Button(frame1, text="start", command=lambda: on_start())
  Button(frame1, text="reset", command=lambda: on_reset())
  Label(win, text=0) #widget displaying the counter

  win.startButton = win[0][0] #capturing start button
  win.label = win[1] #capturing label
  
  # ----------------------------------------------------------------------------
  win.after(0, tick)
  # ----------------------------------------------------------------------------
  win.loop()
# ------------------------------------------------------------------------------
if __name__ == '__main__':
  main()
# ==============================================================================