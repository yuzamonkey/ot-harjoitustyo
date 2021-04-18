import tkinter as tk
from utils.colors import LIGHT_GRAY, GRAY, DARK_GREY
from services.file_service import file_service
from services.score_service import score_service

class StartupOptions:
  def __init__(self, parent_frame, show_layout):
    self._frame = tk.Frame(master=parent_frame, bg=LIGHT_GRAY)
    self._frame.pack(fill=tk.BOTH, expand=True)
    self._frame.columnconfigure([0,1,2], weight=1)
    self._frame.rowconfigure([0,1,2,3], weight=1)
    self._startup_options_frame = tk.Frame(
      master=self._frame,
      width=500,
      height=250,
      bg=GRAY,
      highlightbackground=DARK_GREY,
      highlightthickness=1
    )
    self._startup_options_frame.grid(row=1, column=1)
    self._startup_options_frame.grid_propagate(False)

    self._startup_options_frame.columnconfigure([0,1], weight=1)
    self._startup_options_frame.rowconfigure([0], weight=1)

    self._show_layout = show_layout

  def show(self):
    self._show_startup_options()

  def destroy(self):
    self._frame.destroy()

  def _handle_create_new_score(self):
    score_service.set_score(file_service.create_new_score())
    self._show_layout()

  def _handle_open_existing_score(self):
    pass

  def _show_startup_options(self):
    new_score_button = tk.Button(
      master=self._startup_options_frame,
      text='New score',
      command=self._handle_create_new_score
    )
    existing_score_button = tk.Button(
      master=self._startup_options_frame,
      text='Open existing score (no functionality yet)',
      command=self._handle_open_existing_score
    )
    new_score_button.grid(row=0, column=0)
    existing_score_button.grid(row=0, column=1)
