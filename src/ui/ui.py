import tkinter as tk
from utils.colors import ui_background
from ui.ribbon import Ribbon
from ui.workspace import Workspace

class UI:
  def __init__(self, root):
    self._root = root
    self._frame = tk.Frame(master=self._root)

  def show(self):
    self._show_layout()

  def _show_layout(self):
    self._frame.pack(fill=tk.BOTH, expand=True)
    
    # Ribbon
    ribbon_frame = tk.Frame(master=self._frame)
    ribbon_frame.pack(fill=tk.X, side=tk.TOP)
    ribbon = Ribbon(ribbon_frame)
    ribbon.show()
    
    # Workspace
    workspace_frame = tk.Frame(master=self._frame, bg=ui_background)
    workspace_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
    workspace = Workspace(workspace_frame)
    workspace.show()

