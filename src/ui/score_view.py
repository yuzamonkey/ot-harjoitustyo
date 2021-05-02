import tkinter as tk
from utils.colors import LIGHT_GRAY
from services.score_service import score_service

class ScoreView:
  def __init__(self, parent_frame):
    self._score = score_service.get_score()
    self._frame = parent_frame
    self._title_frame = None
    self._score_frame = None

  def show(self):
    self.update()
    self._show_title()
    self._show_score()

  def destroy(self):
    self._frame.destroy()

  def update(self):
    self._score = score_service.get_score()

    if self._title_frame:
      self._title_frame.destroy()
    self._title_frame = tk.Frame(master=self._frame, height=50, bg='red')
    self._title_frame.pack(fill=tk.X, side=tk.TOP)
    self._title_frame.pack_propagate(0)
    self._show_title()

    if self._score_frame:
      self._score_frame.destroy()
    self._score_frame = tk.Frame(master=self._frame, bg='green')
    self._score_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
    self._show_score()

  def _show_title(self):
    score_title = tk.Label(master=self._title_frame, text=self._score.get_title(), pady=20)
    score_title.pack()

  def _show_score(self):
    for i in range (0, len(self._score.get_staff().get_measures())):
      measure = tk.Label(
        master=self._score_frame,
        text=f'Measure {i+1}:\n{str(self._score.get_staff().get_measures()[i])}')
      measure.grid(row=0, column=i)
