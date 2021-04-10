from tkinter import ttk, StringVar, constants

class MainView:
  def __init__(self, root):
    self._root = root
    self._frame = None
    self._initialize()

  def _initialize(self):
    self._frame = ttk.Label(master=self._root, text="Hello world!")

  def pack(self):
    self._frame.pack()