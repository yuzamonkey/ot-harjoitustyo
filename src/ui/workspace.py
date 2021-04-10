import tkinter as tk
from utils.colors import navigation_background
from utils.colors import options_view_background

class Workspace:
  def __init__(self, parent_frame):
    self._frame = parent_frame

  def show(self):
    self._show_workspace()

  def _show_workspace(self):
    workspace_label = tk.Label(master=self._frame, text='Workspace')
    workspace_label.grid(row=0, column=0)

