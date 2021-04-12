import tkinter as tk

class ScoreView:
  def __init__(self, parent_frame, score_to_edit):
    self._frame = parent_frame
    self._score_to_edit = score_to_edit

  def show(self):
    self._show_score_view()

  def destroy(self):
    self._frame.destroy()

  def _show_score_view(self):
    label = tk.Label(master=self._frame, text=f'ScoreView: {str(self._score_to_edit)}')
    label.grid(row=1, column=1)
    