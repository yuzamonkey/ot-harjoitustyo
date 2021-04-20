import tkinter as tk
from services.score_service import score_service
from utils.constants import NOTATION_LENGTHS, PITCHES

class NotationOptions:
  def __init__(self, frame, update_score_view):
    self._frame = frame
    self._update_score_view = update_score_view

    self._selected_entry = None

  def show(self):
    self._show_notation_options()

  def destroy(self):
    self._frame.destroy()

  def _destroy_selected_entry(self):
    if self._selected_entry:
      self._selected_entry.destroy()

  def _handle_add_measure(self):
    score_service.add_measure()
    self._update_score_view()

  def _handle_remove_last_measure(self):
    score_service.remove_last_measure()
    self._update_score_view()

  def _handle_add_note(self, measure, length, pitch):
    is_success = score_service.add_note(measure, length, pitch)
    if is_success:
      self._update_score_view()

  def _handle_add_rest(self, measure, length):
    is_success = score_service.add_rest(measure, length)
    if is_success:
      self._update_score_view()

  def _show_add_note_options(self):
    self._destroy_selected_entry()
    self._selected_entry = AddNoteOptions(self._frame, self._handle_add_note)
    self._selected_entry.show()

  def _show_add_rest_options(self):
    self._destroy_selected_entry()
    self._selected_entry = AddRestOptions(self._frame, self._handle_add_rest)
    self._selected_entry.show()

  def _show_notation_options(self):
    add_measure_button = tk.Button(master=self._frame,
      text="Add measure",
      command=self._handle_add_measure
      )
    add_measure_button.grid(row=0, column=0)

    remove_last_measure_button = tk.Button(master=self._frame,
      text="Remove last measure",
      command=self._handle_remove_last_measure
      )
    remove_last_measure_button.grid(row=0, column=1)

    add_rest_button = tk.Button(master=self._frame,
      text="Add note",
      command=self._show_add_note_options
      )
    add_rest_button.grid(row=0, column=2)

    add_rest_button = tk.Button(master=self._frame,
      text="Add rest",
      command=self._show_add_rest_options
      )
    add_rest_button.grid(row=0, column=3)


class AddNoteOptions:
  def __init__(self, frame, handle_add_note):
    self._frame = tk.Frame(master=frame)
    self._frame.grid(row=0, column=4)
    self._handle_add_note = handle_add_note

  def destroy(self):
    self._frame.destroy()

  def show(self):
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
        pitch_clicked.get()
        )
      )

    measure_drop.grid(row=0, column=0)
    length_drop.grid(row=0, column=1)
    pitch_drop.grid(row=0, column=2)
    add_button.grid(row=0, column=3)

class AddRestOptions:
  def __init__(self, frame, handle_add_rest):
    self._frame = tk.Frame(master=frame)
    self._frame.grid(row=0, column=4)
    self._handle_add_rest = handle_add_rest

  def destroy(self):
    self._frame.destroy()

  def show(self):
    measure_numbers = score_service.get_measure_numbers()

    measure_clicked = tk.StringVar()
    measure_clicked.set("Select measure")
    measure_drop = tk.OptionMenu(self._frame, measure_clicked, *measure_numbers )

    length_clicked = tk.StringVar()
    length_clicked.set("Select length")
    length_drop = tk.OptionMenu(self._frame, length_clicked, *NOTATION_LENGTHS )

    add_button = tk.Button(
      master=self._frame,
      text="Add",
      command=lambda: self._handle_add_rest(
        measure_clicked.get(),
        length_clicked.get()
        )
      )

    measure_drop.grid(row=0, column=0)
    length_drop.grid(row=0, column=1)
    add_button.grid(row=0, column=2)
