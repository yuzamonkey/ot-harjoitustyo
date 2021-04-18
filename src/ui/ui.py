import tkinter as tk
from ui.ribbon import Ribbon
from ui.startup_options import StartupOptions
from ui.score_view import ScoreView

class UI:
  def __init__(self, root):
    self._root = root
    self._frame = tk.Frame(master=self._root)
    self._frame.pack(fill=tk.BOTH, expand=True)
    self._score = None

    self._startup_frame = tk.Frame(master=self._frame)
    self._startup_frame.pack(fill=tk.BOTH, expand=True)

    self._ribbon_frame = tk.Frame(master=self._frame)
    self._scoreview_frame = tk.Frame(master=self._frame)
    self._ribbon = Ribbon(self._ribbon_frame)
    self._score_view = ScoreView(self._scoreview_frame, self._score)

  def show(self):
    self._show_startup_options()

  def _update_score_view(self):
    self._score_view.destroy()
    self._score_view = ScoreView(self._scoreview_frame, self._score)
    self._score_view.show()

  def _set_score(self, score):
    self._score = score
    self._update_score_view()

  def _show_startup_options(self):
    startup_options = StartupOptions(
      self._startup_frame,
      self._show_layout,
      self._set_score
      )
    startup_options.show()

  def _show_layout(self):
    self._startup_frame.destroy()
    self._frame.pack(fill=tk.BOTH, expand=True)
    self._ribbon_frame.pack(fill=tk.X, side=tk.TOP)
    self._scoreview_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
    self._ribbon.show()
    self._score_view.show()
