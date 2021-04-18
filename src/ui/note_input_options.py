import tkinter as tk

class NoteInputOptions:
  def __init__(self, frame):
    self._frame = frame

  def show(self):
    self._show_note_input_options()

  def _show_note_input_options(self):
    label = tk.Label(master=self._frame, text="SHOW NOTE INPUT")
    label.grid(row=0, column=0)