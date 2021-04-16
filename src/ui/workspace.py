import tkinter as tk
from ui.startup_options import StartupOptions
from ui.score_view import ScoreView

class Workspace:
  def __init__(self, parent_frame, score_to_edit):
    self._frame = tk.Frame(master=parent_frame)
    self._frame.pack(fill=tk.BOTH, expand=True)
    self._score_to_edit = score_to_edit

  def _set_score_to_edit(self, score):
    self._score_to_edit = score

  def show(self):
    self._show_score_view()

  def _show_score_view(self):
    self._score_view = ScoreView(self._frame, self._score_to_edit)
    self._score_view.show()
