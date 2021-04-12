import tkinter as tk

class ScoreView:
  def __init__(self, parent_frame):
    self._frame = parent_frame

  def show(self):
    self._show_score_view()

  def destroy(self):
    self._frame.destroy()

  def _show_score_view(self):
    label = tk.Label(master=self._frame, text='show score here')
    label.grid(row=1, column=1)