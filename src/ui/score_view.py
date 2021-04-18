import tkinter as tk
from utils.colors import LIGHT_GRAY

class ScoreView:
  def __init__(self, parent_frame, score_to_edit):
    self._frame = tk.Frame(master=parent_frame, bg=LIGHT_GRAY)
    self._frame.pack(fill=tk.BOTH, expand=True)
    self._score = score_to_edit

  def show(self):
    self._show_score_view()

  def destroy(self):
    self._frame.destroy()

  def _show_score_view(self):
    score_title = tk.Label(master=self._frame, text=self._score.get_title())
    score_title.grid(row=0, column=0)
    for i in range (0, len(self._score.get_staff().get_measures())):
      measure = tk.Label(master=self._frame, text=str(self._score.get_staff().get_measures()[i]))
      measure.grid(row=1, column=i)
