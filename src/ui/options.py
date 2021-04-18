import tkinter as tk

class Options:
  def __init__(self, options_frame):
    self._parent_frame = options_frame
    self._frame = tk.Frame(master=self._parent_frame)

  def _set_options_frame(self):
    self._frame.destroy()
    self._frame = tk.Frame(master=self._parent_frame)
    self._frame.grid()

  def show_note_input(self):
    self._set_options_frame()
    label = tk.Label(master=self._frame, text="SHOW NOTE INPUT")
    label.grid(row=0, column=0)

  def show_signatures(self):
    self._set_options_frame()
    label = tk.Label(master=self._frame, text="SHOW SIGNATURES")
    label.grid(row=0, column=0)

  def show_tools(self):
    self._set_options_frame()
    label = tk.Label(master=self._frame, text="TOOLS")
    label.grid(row=0, column=0)