import tkinter as tk
from services.score_service import score_service

class ToolsOptions:
  def __init__(self, frame, update_score_view):
    self._frame = frame
    self._update_score_view = update_score_view

  def show(self):
    self._show_tools_options()

  def destroy(self):
    self._frame.destroy()

  def _handle_title_change(self, title):
    score_service.set_title(title)
    self._update_score_view()

  def _show_tools_options(self):
    change_title_label = tk.Label(master=self._frame, text="Change title:")
    change_title_entry = tk.Entry(master=self._frame)
    change_title_button = tk.Button(master=self._frame, text="Change", command=lambda: self._handle_title_change(change_title_entry.get()))
    change_title_label.grid(row=0, column=0)
    change_title_entry.grid(row=0, column=1)
    change_title_button.grid(row=0, column=2)
