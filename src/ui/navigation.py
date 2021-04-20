import tkinter as tk

class Navigation:
  def __init__(self, navigation_frame, show_note_input, show_signatures, show_tools):
    self._frame = navigation_frame
    self._show_note_input = show_note_input
    self._show_signatures = show_signatures
    self._show_tools = show_tools

  def show(self):
    self._show_navigation()

  def _show_navigation(self):
    note_input_button = tk.Button(
      master=self._frame,
      text='Notation',
      command=self._show_note_input
      )
    signatures_button = tk.Button(
      master=self._frame,
      text='Signatures',
      command=self._show_signatures
      )
    tools_button = tk.Button(
      master=self._frame,
      text='Tools',
      command=self._show_tools
      )
    note_input_button.grid(row=0, column=0)
    signatures_button.grid(row=0, column=1)
    tools_button.grid(row=0, column=2)
