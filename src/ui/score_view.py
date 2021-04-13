import tkinter as tk

class ScoreView:
  def __init__(self, parent_frame, score_to_edit):
    self._frame = parent_frame
    self._score = score_to_edit

  def show(self):
    self._show_score_view()

  def destroy(self):
    self._frame.destroy()

  def _show_score_view(self):
    score_title = tk.Label(master=self._frame, text=self._score.get_title())
    score_title.grid(row=0, column=1)
    label = tk.Label(master=self._frame, text=str(self._score))
    label.grid(row=1, column=1)
    