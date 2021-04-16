import tkinter as tk
from utils.colors import DARK_BLUE, GRAY

class Ribbon:
  def __init__(self, parent_frame, add_measure):
    self._frame = parent_frame
    self._frame.columnconfigure(0, weight=1)
    self._frame.rowconfigure([0,1], weight=1)
    self._navigation_frame = tk.Frame(master=self._frame, height=50, bg=DARK_BLUE)
    self._options_frame = tk.Frame(master=self._frame, height=50, bg=GRAY)

    self._navigation_frame.grid(row=0, column=0, sticky='new')
    self._options_frame.grid(row=1, column=0, sticky='esw')
    self._navigation_frame.grid_propagate(False)
    self._options_frame.grid_propagate(False)

    self._selected_options_frame = None
    self._show_note_input()

    self._add_measure = add_measure

  def show(self):
    self._show_ribbon()

  def _handle_add_measure(self):
    self._add_measure()

  def _set_selected_options_frame(self):
    if self._selected_options_frame:
      self._selected_options_frame.destroy()
    self._selected_options_frame = tk.Frame(master=self._options_frame)
    self._selected_options_frame.grid()

  def _show_note_input(self):
    self._set_selected_options_frame()
    label = tk.Label(master=self._selected_options_frame, text="note input")
    label.grid(row=0, column=0)
    add_measure_button = tk.Button(
      master=self._selected_options_frame,
      text='Add measure',
      command=self._handle_add_measure
      )
    add_measure_button.grid(row=0, column=1)


  def _show_signatures(self):
    self._set_selected_options_frame()
    label = tk.Label(master=self._selected_options_frame, text="signatures")
    label.grid(row=0, column=0)

  def _show_tools(self):
    self._set_selected_options_frame()
    label = tk.Label(master=self._selected_options_frame, text="tools")
    label.grid(row=0, column=0)

  def _show_ribbon(self):
    note_input_button = tk.Button(
      master=self._navigation_frame,
      text='Notes',
      command=self._show_note_input
      )
    signatures_button = tk.Button(
      master=self._navigation_frame,
      text='Signatures',
      command=self._show_signatures
      )
    tools_button = tk.Button(
      master=self._navigation_frame,
      text='Tools',
      command=self._show_tools
      )
    note_input_button.grid(row=0, column=0)
    signatures_button.grid(row=0, column=1)
    tools_button.grid(row=0, column=2)
