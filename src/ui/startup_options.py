import tkinter as tk
from utils.colors import gray, dark_gray
from services.file_service import file_service

class StartupOptions:
  def __init__(self, parent_frame, show_score_view):
    self._frame = parent_frame
    self._show_score_view = show_score_view
    
    self._startup_options_frame = tk.Frame(master=self._frame, width=500, height=250, bg=gray, highlightbackground=dark_gray, highlightthickness=1)
    self._startup_options_frame.grid(row=1, column=1)
    self._startup_options_frame.grid_propagate(False)

    self._startup_options_frame.columnconfigure([0,1], weight=1)
    self._startup_options_frame.rowconfigure([0], weight=1)

  def show(self):
    self._show_startup_options()

  def destroy(self):
    self._startup_options_frame.destroy()

  def _handle_create_new_file(self):
    file_service.create_new_file()
    self._show_score_view()

  def _handle_open_existing_file(self):
    file_service.open_existing_file()

  def _show_startup_options(self):
    new_file_button = tk.Button(master=self._startup_options_frame, text='New file', command=self._handle_create_new_file)
    existing_file_button = tk.Button(master=self._startup_options_frame, text='Open existing file (no functionality yet)', command=self._handle_open_existing_file)
    
    new_file_button.grid(row=0, column=0)
    existing_file_button.grid(row=0, column=1)


