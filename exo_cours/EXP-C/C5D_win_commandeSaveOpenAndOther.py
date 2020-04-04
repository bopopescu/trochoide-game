# ==============================================================================
"""WIN : demo program for window manipulations"""
# ==============================================================================
__author__  = "Christophe Schlick"
__version__ = "4.0" # test some standard dialog windows
__date__    = "2018-01-15"
# ==============================================================================
from ezTK import *
# ------------------------------------------------------------------------------
def message(text):
  """change message shown on status bar"""
  win.label['text'] = text
# ------------------------------------------------------------------------------
def on_info():
  """callback for the "INFO" button"""
  message("INFO button has been pressed")
  MessageDialog.showinfo('INFO', message='This is an information message')
  message("INFO window has been closed")
# ------------------------------------------------------------------------------
def on_warn():
  """callback for the "WARN" button"""
  message("WARN button has been pressed")
  MessageDialog.showwarning('WARN', message='This is a warning message')
  message("WARN window has been closed")
# ------------------------------------------------------------------------------
def on_error():
  """callback for the "ERROR" button"""
  message("ERROR button has been pressed")
  MessageDialog.showerror('ERROR', message='This is an error message')
  message("ERROR window has been closed")
# ------------------------------------------------------------------------------
def on_yesno():
  """callback for the "YES-NO" button"""
  message("YES/NO button has been pressed")
  val = MessageDialog.askyesno('YES-NO', message='Select YES or NO')
  message("Value = %s" % val)
# ------------------------------------------------------------------------------
def on_color():
  """callback for the "COLOR" button"""
  message("COLOR button has been pressed")
  val = ColorDialog.askcolor()
  message("RGB = %s Color = %s" % val)
# ------------------------------------------------------------------------------
def on_open():
  """callback for the "OPEN FILE" button"""
  message("OPEN FILE button has been pressed")
  val = FileDialog.askopenfilename(title='OPEN FILE')
  message("File = %s" % val)
# -----------------------------------------------------------------------------
def on_save():
  """callback for the "SAVE FILE" button"""
  message("SAVE FILE button has been pressed")
  val = FileDialog.askSaveAsFileName(title='SAVE FILE')
  message("File = %s" % val)
# ------------------------------------------------------------------------------
def on_popup():
  """callback for the "POPUP" button"""
  message("POPUP button has been pressed")
  popup = Win(win, title='POPUP', flow='E', op=10)
  Label(popup, text='This is a modal window\n\nPlease close it to continue',
    width=20, height=3, relief='flat')
  popup.wait() # wait until popup window has been closed
  message("POPUP window has been closed")
# ------------------------------------------------------------------------------
def main():
  """create the main window and pack the widgets"""
  global win
  win = Win(title='DIALOG', grow=False, fold=4, op=2)
  # ----------------------------------------------------------------------------
  Button(win, text='INFO', width=12, command=on_info)
  Button(win, text='WARN', width=12, command=on_warn)
  Button(win, text='ERROR', width=12, command=on_error)
  Button(win, text='YES-NO', width=12, command=on_yesno)
  Button(win, text='COLOR', width=12, command=on_color)
  Button(win, text='OPEN FILE', width=12, command=on_open)
  Button(win, text='SAVE FILE', width=12, command=on_save)
  Button(win, text='POPUP', width=12, command=on_popup)
  # ----------------------------------------------------------------------------
  win.label = Label(win, text='', relief='groove', anchor='W')
  win.loop()
# ==============================================================================
if __name__ == '__main__':
  main()
# ==============================================================================
