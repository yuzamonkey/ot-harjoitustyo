import tkinter as tk
from services.score_service import score_service
from services.file_service import file_service
from services.playback_service import playback_service

class ToolsOptions:
  def __init__(self, frame, update_score_view, show_startup_options):
    self._frame = frame
    self._update_score_view = update_score_view
    self._show_startup_options = show_startup_options

  def show(self):
    self._show_tools_options()

  def destroy(self):
    self._frame.destroy()

  def _handle_title_change(self, title):
    score_service.set_title(title)
    self._update_score_view()

  def _handle_play(self):
    playback_service.play()

  def _handle_stop(self):
    playback_service.stop()

  def _handle_save_score(self):
    file_service.save_file()

  def _handle_show_startup(self):
    self._show_startup_options()

  def _show_tools_options(self):
    change_title_label = tk.Label(master=self._frame, text="Change title:")
    change_title_entry = tk.Entry(master=self._frame)
    change_title_button = tk.Button(
      master=self._frame,
      text="Change",
      command=lambda: self._handle_title_change(change_title_entry.get())
      )
    change_title_label.grid(row=0, column=0)
    change_title_entry.grid(row=0, column=1)
    change_title_button.grid(row=0, column=2)

    play_button = tk.Button(
      master=self._frame,
      text="Play",
      command=self._handle_play
    )

    play_button.grid(row=0, column=3)

    stop_button = tk.Button(
      master=self._frame,
      text="Stop",
      command=self._handle_stop
    )

    stop_button.grid(row=0, column=4)
    
    save_button = tk.Button(
      master=self._frame,
      text="Save score",
      command=self._handle_save_score
    )
    save_button.grid(row=0, column=5)

    show_startup_button = tk.Button(
      master=self._frame,
      text="Show startup",
      command=self._handle_show_startup
    )
    show_startup_button.grid(row=0, column=6)
