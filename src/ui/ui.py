from tkinter import Tk, ttk
from ui.main_view import MainView

class UI:
  def __init__(self, root):
    self._root = root
    self._current_view = None

  def start(self):
    self._hide_current_view()
    self._show_main_view()

  def _hide_current_view(self):
    if self._current_view:
      self._current_view.destroy()
    self._current_view = None

  def _show_main_view(self):
    self._hide_current_view()
    self._current_view = MainView(self._root)
    self._current_view.pack()
