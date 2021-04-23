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
    self._startup_options_frame.pack_propagate(0)

    self._buttons_frame = None
    # self._buttons_frame.pack(fill=tk.BOTH, expand=1)
    # self._buttons_frame.grid_propagate(False)

    # self._buttons_frame.columnconfigure([0,1], weight=1)
    # self._buttons_frame.rowconfigure([0], weight=1)

    self._score_selection_frame = None

    self._show_layout = show_layout

  def show(self):
    self._show_startup_options()

  def destroy(self):
    self._frame.destroy()

  def _update_score_selection(self):
    self._score_selection_frame.destroy()
    self._score_selection_frame = None
    self._show_score_selection()

  def _handle_create_new_score(self):
    score_service.set_score(file_service.create_new_score())
    self._show_layout()

  def _handle_open_score(self, score_title):
    score = file_service.get_score_object(score_title)
    score_service.set_score(score)
    self._show_layout()

  def _handle_delete_score(self, score_title):
    file_service.delete_score(score_title)
    self._update_score_selection()

  def _handle_back(self):
    self._score_selection_frame.destroy()
    self._show_startup_options()

  def _show_score_selection(self):
    self._buttons_frame.destroy()
    score_titles = file_service.get_score_names()
    
    self._score_selection_frame = tk.Frame(master=self._startup_options_frame, bg=GRAY)
    self._score_selection_frame.pack(fill=tk.BOTH, expand=1)

    back_button = tk.Button(master=self._score_selection_frame, text="Back", command=self._handle_back)
    back_button.pack(side=tk.BOTTOM)

    canvas = tk.Canvas(master=self._score_selection_frame, bg=GRAY)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    scrollbar = tk.Scrollbar(master=self._score_selection_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox("all")))

    canvas_frame = tk.Frame(master=canvas)
    canvas.create_window((0,0), window=canvas_frame, anchor="nw")

    for i in range(len(score_titles)):
      name_label = tk.Label(master=canvas_frame, text=score_titles[i])
      open_button = tk.Button(master=canvas_frame, text=f"Open", command=lambda i=i: self._handle_open_score(score_titles[i]))
      delete_button = tk.Button(master=canvas_frame, text=f"Delete", command=lambda i=i: self._handle_delete_score(score_titles[i]))
      
      name_label.grid(row=i, column=0)
      open_button.grid(row=i, column=1)
      delete_button.grid(row=i, column=2)

  def _show_startup_options(self):
    self._buttons_frame = tk.Frame(master=self._startup_options_frame, bg=GRAY)
    self._buttons_frame.pack(fill=tk.BOTH, expand=1)
    self._buttons_frame.grid_propagate(False)

    self._buttons_frame.columnconfigure([0,1], weight=1)
    self._buttons_frame.rowconfigure([0], weight=1)
    new_score_button = tk.Button(
      master=self._buttons_frame,
      text='New score',
      command=self._handle_create_new_score
    )
    existing_score_button = tk.Button(
      master=self._buttons_frame,
      text='Saved scores',
      command=self._show_score_selection
    )
    new_score_button.grid(row=0, column=0)
    existing_score_button.grid(row=0, column=1)
