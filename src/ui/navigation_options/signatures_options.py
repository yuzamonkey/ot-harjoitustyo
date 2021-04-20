import tkinter as tk
from services.score_service import score_service
from utils.constants import CLEFS, TIME_SIGNATURES, KEY_SIGNATURES

class SignaturesOptions:
  def __init__(self, frame, update_score_view):
    self._frame = frame
    self._update_score_view = update_score_view

    self._selected_entry = None

  def show(self):
    self._show_signatures_options()

  def destroy(self):
    self._frame.destroy()

  def _destroy_selected_entry(self):
    if self._selected_entry:
      self._selected_entry.destroy()

  def _handle_clef_change(self, clef):
    is_success = score_service.change_clef(clef)
    if is_success:
      self._update_score_view()

  def _handle_key_change(self, key):
    is_success = score_service.change_key(key)
    if is_success:
      self._update_score_view()

  def _handle_time_change(self, time_signature):
    is_success = score_service.change_time_signature(time_signature)
    if is_success:
      self._update_score_view()

  def _show_change_clef_options(self):
    self._destroy_selected_entry()
    self._selected_entry = ChangeClefOptions(self._frame, self._handle_clef_change)
    self._selected_entry.show()

  def _show_change_key_options(self):
    self._destroy_selected_entry()
    self._selected_entry = ChangeKeySignatureOptions(self._frame, self._handle_key_change)
    self._selected_entry.show()

  def _show_change_time_options(self):
    self._destroy_selected_entry()
    self._selected_entry = ChangeTimeSignatureOptions(self._frame, self._handle_time_change)
    self._selected_entry.show()

  def _show_signatures_options(self):
    change_clef_button = tk.Button(master=self._frame,
      text="Change clef",
      command=self._show_change_clef_options
      )
    change_clef_button.grid(row=0, column=0)

    change_key_button = tk.Button(master=self._frame,
      text="Change key signature",
      command=self._show_change_key_options
      )
    change_key_button.grid(row=0, column=1)

    change_time_signature_button = tk.Button(master=self._frame,
      text="Change time signature",
      command=self._show_change_time_options
      )
    change_time_signature_button.grid(row=0, column=2)

class ChangeClefOptions:
  def __init__(self, frame, handle_clef_change):
    self._frame = tk.Frame(master=frame)
    self._frame.grid(row=0, column=3)

    self._handle_clef_change = handle_clef_change

  def destroy(self):
    self._frame.destroy()

  def show(self):
    clef_picked = tk.StringVar()
    clef_picked.set("Select clef")
    clef_drop = tk.OptionMenu(self._frame, clef_picked, *CLEFS )

    change_button = tk.Button(
      master=self._frame,
      text="Change",
      command=lambda: self._handle_clef_change(
        clef_picked.get()
        )
      )
    clef_drop.grid(row=0, column=3)
    change_button.grid(row=0, column=4)

class ChangeKeySignatureOptions:
  def __init__(self, frame, handle_key_change):
    self._frame = tk.Frame(master=frame)
    self._frame.grid(row=0, column=3)

    self._handle_key_change = handle_key_change

  def destroy(self):
    self._frame.destroy()

  def show(self):
    key_picked = tk.StringVar()
    key_picked.set("Select key")
    key_drop = tk.OptionMenu(self._frame, key_picked, *KEY_SIGNATURES )

    change_button = tk.Button(
      master=self._frame,
      text="Change",
      command=lambda: self._handle_key_change(
        key_picked.get()
        )
      )
    key_drop.grid(row=0, column=3)
    change_button.grid(row=0, column=4)

class ChangeTimeSignatureOptions:
  def __init__(self, frame, handle_time_change):
    self._frame = tk.Frame(master=frame)
    self._frame.grid(row=0, column=3)

    self._handle_time_change = handle_time_change

  def destroy(self):
    self._frame.destroy()

  def show(self):
    time_picked = tk.StringVar()
    time_picked.set("Select time signature")
    time_drop = tk.OptionMenu(self._frame, time_picked, *TIME_SIGNATURES )

    change_button = tk.Button(
      master=self._frame,
      text="Change",
      command=lambda: self._handle_time_change(
        time_picked.get()
        )
      )
    time_drop.grid(row=0, column=3)
    change_button.grid(row=0, column=4)
