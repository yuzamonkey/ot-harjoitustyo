import tkinter as tk

class ToolsOptions:
  def __init__(self, frame):
    self._frame = frame

  def show(self):
    self._show_tools_options()

  def destroy(self):
    self._frame.destroy()

  def _show_tools_options(self):
    label = tk.Label(master=self._frame, text="TOOLS")
    label.grid(row=0, column=0)
