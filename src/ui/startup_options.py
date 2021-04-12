import tkinter as tk
from utils.colors import gray, dark_gray
from services.file_service import file_service

class StartupOptions:
  def __init__(self, parent_frame, show_score_view, set_score_to_edit):
    self._frame = parent_frame
    self._show_score_view = show_score_view
    self._set_score_to_edit = set_score_to_edit

    self._startup_options_frame = tk.Frame(master=self._frame, width=500, height=250, bg=gray, highlightbackground=dark_gray, highlightthickness=1)
    self._startup_options_frame.grid(row=1, column=1)
    self._startup_options_frame.grid_propagate(False)

    self._startup_options_frame.columnconfigure([0,1], weight=1)
    self._startup_options_frame.rowconfigure([0], weight=1)

  def show(self):
    self._show_startup_options()

  def destroy(self):
    self._startup_options_frame.destroy()

  def _handle_create_new_score(self):
    self._set_score_to_edit(file_service.create_new_score())
    self._show_score_view()

  def _handle_open_existing_score(self):
    file_service.open_existing_score()

  def _show_startup_options(self):
    new_score_button = tk.Button(master=self._startup_options_frame, text='New score', command=self._handle_create_new_score)
    existing_score_button = tk.Button(master=self._startup_options_frame, text='Open existing score (no functionality yet)', command=self._handle_open_existing_score)
    
    new_score_button.grid(row=0, column=0)
    existing_score_button.grid(row=0, column=1)

