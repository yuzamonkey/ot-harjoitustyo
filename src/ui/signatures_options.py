import tkinter as tk

class SignaturesOptions:
  def __init__(self, frame):
    self._frame = frame

  def show(self):
    self._show_signatures_options()

  def _show_signatures_options(self):
    label = tk.Label(master=self._frame, text="SHOW SIGNATURES")
    label.grid(row=0, column=0)