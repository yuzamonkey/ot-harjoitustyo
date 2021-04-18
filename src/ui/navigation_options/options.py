import tkinter as tk
from ui.navigation_options.notation_options import NotationOptions
from ui.navigation_options.signatures_options import SignaturesOptions
from ui.navigation_options.tools_options import ToolsOptions

class Options:
  def __init__(self, options_frame, update_score_view):
    self._parent_frame = options_frame
    self._frame = tk.Frame(master=self._parent_frame)
    self._update_score_view = update_score_view

  def _set_options_frame(self):
    self._frame.destroy()
    self._frame = tk.Frame(master=self._parent_frame)
    self._frame.grid()

  def show_note_input(self):
    self._set_options_frame()
    note_input_options = NotationOptions(self._frame, self._update_score_view)
    note_input_options.show()

  def show_signatures(self):
    self._set_options_frame()
    signatures_options = SignaturesOptions(self._frame)
    signatures_options.show()

  def show_tools(self):
    self._set_options_frame()
    tools_options = ToolsOptions(self._frame)
    tools_options.show()
    