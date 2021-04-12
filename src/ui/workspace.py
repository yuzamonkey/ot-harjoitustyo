import tkinter as tk
from ui.startup_options import StartupOptions
from ui.score_view import ScoreView

class Workspace:
  def __init__(self, parent_frame):
    self._frame = parent_frame
    self._frame.columnconfigure([0,1,2], weight=1)
    self._frame.rowconfigure([0,1,2,3], weight=1)
    self._current_view = None

  def show(self):
    self._show_startup_options()
    #self._show_score_view()

  def _hide_current_view(self):
    if self._current_view:
      self._current_view.destroy()
    self._current_view = None      

  def _show_startup_options(self):
    self._current_view = StartupOptions(self._frame, self._show_score_view)
    self._current_view.show()


  def _show_score_view(self):
    self._hide_current_view()
    self._current_view = ScoreView(self._frame)
    self._current_view.show()

