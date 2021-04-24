import tkinter as tk
from ui.ui import UI

import os

def main():
  root = tk.Tk()
  root.title("Nuotinnussofta")
  root.geometry("1200x800")
  root.minsize(600, 400)
  ui = UI(root)
  ui.show()
  root.mainloop()

if __name__ == '__main__':
  main()
