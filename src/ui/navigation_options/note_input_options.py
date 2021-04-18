import tkinter as tk
from services.score_service import score_service

class NoteInputOptions:
  def __init__(self, frame):
    self._frame = frame

  def show(self):
    self._show_note_input_options()

  def destroy(self):
    self._frame.destroy()

  def _handle_add_measure(self):
    score_service.add_measure()
    # listener to score view??

  def _show_note_input_options(self):
    label = tk.Label(master=self._frame, text="SHOW NOTE INPUT")
    label.grid(row=0, column=0)
    add_measure_button = tk.Button(master=self._frame,
      text="Add measure",
      command=self._handle_add_measure
      )
    add_measure_button.grid(row=0, column=1)
