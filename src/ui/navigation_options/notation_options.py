import tkinter as tk
from services.score_service import score_service
from utils.constants import NOTATION_LENGTHS, PITCHES

class NotationOptions:
  def __init__(self, frame, update_score_view):
    self._frame = frame
    self._update_score_view = update_score_view

    self._selected_entry = None
    self._error_label = None
    self._update_error_label()

  def show(self):
    self._show_notation_options()

  def destroy(self):
    self._frame.destroy()

  def _update_error_label(self):
    if self._error_label:
      self._error_label.destroy()
    self._error_label = tk.Label(master=self._frame, text="Measure does not have space", fg='red')

  def _destroy_selected_entry(self):
    if self._selected_entry:
      self._selected_entry.destroy()

  def _handle_add_measure(self):
    score_service.add_measure()
    self._update_score_view(1.0)

  def _handle_remove_last_measure(self):
    score_service.remove_last_measure()
    self._update_score_view(1.0)

  def _handle_add_note(self, measure, length, pitch):
    self._update_error_label()
    try:
      is_success = score_service.add_note(measure, length, pitch)
      if is_success == True:
        self._update_score_view((int(measure) - 1) / score_service.get_staff_length())
      elif is_success == 'No space':
        self._error_label.grid(row=0, column=8)
    except:
      pass

  def _handle_add_rest(self, measure, length):
    self._update_error_label()
    try:
      is_success = score_service.add_rest(measure, length)
      if is_success == True:
        self._update_score_view((int(measure) - 1) / score_service.get_staff_length())
      elif is_success == 'No space':
        self._error_label.grid(row=0, column=8)
    except:
      pass

  def _handle_remove_notation(self, selected):
    self._update_error_label()
    try:
      measure_index = int(selected[1:2])
      notation_index = int(selected[5:6])
      score_service.remove_notation(measure_index - 1, notation_index - 1)
      self._selected_entry.update()
      self._update_score_view(measure_index / score_service.get_staff_length())
    except:
      pass

  def _show_add_note_options(self):
    self._update_error_label()
    self._destroy_selected_entry()
    self._selected_entry = AddNoteOptions(self._frame, self._handle_add_note)
    self._selected_entry.show()

  def _show_add_rest_options(self):
    self._update_error_label()
    self._destroy_selected_entry()
    self._selected_entry = AddRestOptions(self._frame, self._handle_add_rest)
    self._selected_entry.show()

  def _show_remove_notation_options(self):
    self._update_error_label()
    self._destroy_selected_entry()
    self._selected_entry = RemoveNotationOptions(self._frame, self._handle_remove_notation)
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

    remove_notation_button = tk.Button(master=self._frame,
      text="Remove notation",
      command=self._show_remove_notation_options
      )
    remove_notation_button.grid(row=0, column=4)

class AddNoteOptions:
  def __init__(self, frame, handle_add_note):
    self._frame = tk.Frame(master=frame)
    self._frame.grid(row=0, column=5)
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
    self._frame.grid(row=0, column=5)
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

class RemoveNotationOptions:
  def __init__(self, frame, handle_remove_notation):
    self._parent_frame = frame
    self._frame = tk.Frame(master=self._parent_frame)
    self._frame.grid(row=0, column=5)
    self._handle_remove_notation = handle_remove_notation

  def destroy(self):
    self._frame.destroy()

  def update(self):
    self.destroy()
    self._frame = tk.Frame(master=self._parent_frame)
    self._frame.grid(row=0, column=5)
    self.show()

  def show(self):
    notations = score_service.get_notations()
    if not notations:
      notations = ['No options']
    
    notation_clicked = tk.StringVar()
    notation_clicked.set("Select notation")
    notation_drop = tk.OptionMenu(self._frame, notation_clicked, *notations )

    remove_button = tk.Button(
      master=self._frame,
      text="Remove",
      command=lambda: self._handle_remove_notation(
        notation_clicked.get()
        )
    )

    notation_drop.grid(row=0, column=0)
    remove_button.grid(row=0, column=1)
