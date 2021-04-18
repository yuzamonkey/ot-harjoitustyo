import tkinter as tk
from utils.colors import DARK_BLUE, GRAY
from ui.navigation import Navigation
from ui.navigation_options.options import Options

class Ribbon:
  def __init__(self, parent_frame):
    self._frame = parent_frame
    self._frame.columnconfigure(0, weight=1)
    self._frame.rowconfigure([0,1], weight=1)
    self._navigation_frame = tk.Frame(master=self._frame, height=50, bg=DARK_BLUE)
    self._options_frame = tk.Frame(master=self._frame, height=50, bg=GRAY)

    self._navigation_frame.grid(row=0, column=0, sticky='new')
    self._options_frame.grid(row=1, column=0, sticky='esw')
    self._navigation_frame.grid_propagate(False)
    self._options_frame.grid_propagate(False)

    self._options = Options(self._options_frame)

  def show(self):
    self._show_ribbon()

  def _show_note_input(self):
    self._options.show_note_input()

  def _show_signatures(self):
    self._options.show_signatures()

  def _show_tools(self):
    self._options.show_tools()

  def _show_ribbon(self):
    navigation = Navigation(
      self._navigation_frame,
      self._show_note_input,
      self._show_signatures,
      self._show_tools
      )
    navigation.show()
    self._options.show_note_input()
