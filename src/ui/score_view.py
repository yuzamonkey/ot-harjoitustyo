import tkinter as tk
from utils.colors import LIGHT_GRAY
from services.score_service import score_service

class ScoreView:
  def __init__(self, parent_frame):
    self._score = score_service.get_score()
    
    self._frame = parent_frame

    self._frame.columnconfigure(0, weight=1)
    self._frame.rowconfigure([0,1], weight=1)

    self._title_frame = tk.Frame(master=self._frame, height=50, bg=LIGHT_GRAY)
    self._title_frame.grid(row=0, column=0, sticky='new')
    self._title_frame.pack_propagate(0)

    self._score_frame = tk.Frame(master=self._frame, bg=LIGHT_GRAY)
    self._score_frame.grid(row=0, column=0)

    
  def show(self):
    self._show_title()
    self._show_score()

  def destroy(self):
    self._frame.destroy()

  def update(self):
    self._score = score_service.get_score()
    self._score_frame.destroy()
    self._score_frame = tk.Frame(master=self._frame)
    self._score_frame.grid(row=0, column=0)
    self._show_score()

  def _show_title(self):
    score_title = tk.Label(master=self._title_frame, text=self._score.get_title())
    score_title.pack()

  def _show_score(self):
    for i in range (0, len(self._score.get_staff().get_measures())):
      measure = tk.Label(master=self._score_frame, text=f'Measure {i+1}:\n{str(self._score.get_staff().get_measures()[i])}')
      measure.grid(row=0, column=i)
