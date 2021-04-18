import tkinter as tk
from services.score_service import score_service

class NotationOptions:
  def __init__(self, frame, update_score_view):
    self._frame = frame
    self._update_score_view = update_score_view

  def show(self):
    self._show_note_input_options()

  def destroy(self):
    self._frame.destroy()

  def _handle_add_measure(self):
    score_service.add_measure()
    self._update_score_view()

  def _handle_add_note(self, measure, length, pitch):
    is_success = score_service.add_note(measure, length, pitch)
    print("ADD NOTE HANDLER RESULT:", is_success)
    self._update_score_view()

  def _show_add_note_entry_form(self):
    measure_label = tk.Label(master=self._frame, text="Measure:")
    length_label = tk.Label(master=self._frame, text="Length:")
    pitch_label = tk.Label(master=self._frame, text="Pitch:")

    measure_entry = tk.Entry(master=self._frame)
    length_entry = tk.Entry(master=self._frame)
    pitch_entry = tk.Entry(master=self._frame)

    add_button = tk.Button(
      master=self._frame, 
      text="Add", 
      command=lambda: self._handle_add_note(
        measure_entry.get(),
        length_entry.get(),
        pitch_entry.get())
        )

    measure_label.grid(row=0, column=3)
    measure_entry.grid(row=0, column=4)
    length_label.grid(row=0, column=5)
    length_entry.grid(row=0, column=6)
    pitch_label.grid(row=0, column=7)
    pitch_entry.grid(row=0, column=8)
    add_button.grid(row=0, column=9)

  def _show_note_input_options(self):
    label = tk.Label(master=self._frame, text="SHOW NOTATION OPTIONS")
    label.grid(row=0, column=0)

    add_measure_button = tk.Button(master=self._frame,
      text="Add measure",
      command=self._handle_add_measure
      )
    add_measure_button.grid(row=0, column=1)
    
    add_note_button = tk.Button(master=self._frame,
      text="Add note",
      command=self._show_add_note_entry_form
      )
    add_note_button.grid(row=0, column=2)
