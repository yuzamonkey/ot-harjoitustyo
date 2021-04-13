import tkinter as tk
from ui.startup_options import StartupOptions
from ui.score_view import ScoreView

class Workspace:
  def __init__(self, parent_frame):
    self._frame = tk.Frame(master=parent_frame)
    self._frame.pack(fill=tk.BOTH, expand=True)
    self._current_view = None
    self._score_to_edit = None

  def _set_score_to_edit(self, score):
    self._score_to_edit = score

  def show(self):
    self._show_startup_options()

  def _hide_current_view(self):
    if self._current_view:
      self._current_view.destroy()
    self._current_view = None

  def _show_startup_options(self):
    self._hide_current_view()
    self._current_view = StartupOptions(self._frame, self._show_score_view, self._set_score_to_edit)
    self._current_view.show()

  def _show_score_view(self):
    self._hide_current_view()
    self._current_view = ScoreView(self._frame, self._score_to_edit)
    self._current_view.show()
