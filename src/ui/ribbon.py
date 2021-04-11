import tkinter as tk
from utils.colors import navigation_background
from utils.colors import options_view_background

class Ribbon:
  def __init__(self, parent_frame):
    self._frame = parent_frame
    self._frame.columnconfigure(0, weight=1)
    self._frame.rowconfigure([0,1], weight=1)

  def show(self):
    self._show_ribbon()

  def _show_ribbon(self):
    # navigation bar
    navigation_frame = tk.Frame(master=self._frame, height=50, bg=navigation_background)
    navigation_label = tk.Label(master=navigation_frame, text="Navigation bar")

    # options
    options_frame = tk.Frame(master=self._frame, height=50, bg=options_view_background)
    options_label = tk.Label(master=options_frame, text="Options")

    navigation_frame.grid(row=0, column=0, sticky='new')
    options_frame.grid(row=1, column=0, sticky='esw')
    navigation_frame.grid_propagate(False)
    options_frame.grid_propagate(False)
    
    navigation_label.grid(row=0, column=0)
    options_label.grid(row=0, column=0)