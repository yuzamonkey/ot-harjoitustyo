import tkinter as tk
from services.score_service import score_service
from utils.constants import NOTATION_LENGTHS, PITCHES

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
    measure_numbers = score_service.get_measure_numbers()

    measure_clicked = tk.StringVar()
    measure_clicked.set("Select measure")
    measure_drop = tk.OptionMenu(self._frame, measure_clicked, *measure_numbers )

    length_clicked = tk.StringVar()
    length_clicked.set("Select length")
    length_drop = tk.OptionMenu(self._frame, length_clicked, *NOTATION_LENGTHS )
    
    pitch_clicked = tk.StringVar()
    pitch_clicked.set("Select pitch")
    pitch_drop = tk.OptionMenu(self._frame, pitch_clicked, *PITCHES )
    
    add_button = tk.Button(
      master=self._frame, 
      text="Add", 
      command=lambda: self._handle_add_note(
        measure_clicked.get(),
        length_clicked.get(),
        pitch_clicked.get())
        )
  
    measure_drop.grid(row=0, column=3)
    length_drop.grid(row=0, column=4)
    pitch_drop.grid(row=0, column=5)
    add_button.grid(row=0, column=6)

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
