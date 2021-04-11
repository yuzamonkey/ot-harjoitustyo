import tkinter as tk
from ui.startup_options import StartupOptions

class Workspace:
  def __init__(self, parent_frame):
    self._frame = parent_frame

  def show(self):
    self._show_workspace()

  def _show_workspace(self):
    # workspace_label = tk.Label(master=self._frame, text='Workspace')
    # workspace_label.grid(row=0, column=0)
    startup_options = StartupOptions(self._frame)
    startup_options.show()

