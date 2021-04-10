import tkinter as tk
from utils.colors import ui_background
from ui.views import Views
from ui.startup_view import StartupView
from ui.ribbon import Ribbon

class UI:
  def __init__(self, root):
    self._root = root
    self._frame = tk.Frame(master=self._root, bg=ui_background)

  def start(self):
    self._show_layout()

  def _show_layout(self):
    self._frame.pack(fill=tk.BOTH, expand=True)
    # Ribbon
    ribbon_frame = tk.Frame(master=self._frame, height=100, bg='red')
    ribbon_frame.pack(fill=tk.constants.X)
    #ribbon_frame.pack_propagate(0) # <- does not allow resizing
    ribbon = Ribbon(ribbon_frame)
    ribbon.show()
    
    # Working view

    # views = Views(self._frame)
    # views.start()
    # self._frame.pack(fill=tk.constants.X)
    # startup = StartupView(self._root)
    # startup.start()
