import tkinter as tk
from ui.ribbon import Ribbon
from ui.workspace import Workspace
from ui.startup_options import StartupOptions

class UI:
  def __init__(self, root):
    self._root = root
    self._frame = tk.Frame(master=self._root)
    self._score_to_edit = None

    self._startup_frame = tk.Frame(master=self._frame)
    self._startup_frame.pack(fill=tk.BOTH, expand=True)

  def show(self):
    self._show_startup_options()
    #self._show_layout()

  def _set_score_to_edit(self, score):
    self._score_to_edit = score

  def _show_startup_options(self):
    self._frame.pack(fill=tk.BOTH, expand=True)
    startup_options = StartupOptions(self._startup_frame, self._show_layout, self._set_score_to_edit)
    startup_options.show()

  def _show_layout(self):
    self._startup_frame.destroy()
    self._frame.pack(fill=tk.BOTH, expand=True)
    # Ribbon
    ribbon_frame = tk.Frame(master=self._frame)
    ribbon_frame.pack(fill=tk.X, side=tk.TOP)
    ribbon = Ribbon(ribbon_frame)
    ribbon.show()
    # Workspace
    workspace_frame = tk.Frame(master=self._frame)
    workspace_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
    workspace = Workspace(workspace_frame, self._score_to_edit)
    workspace.show()
