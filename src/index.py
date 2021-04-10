import tkinter as tk
from ui.ui import UI

def main():
  root = tk.Tk()
  root.title("Nuotinnussofta")
  root.geometry("1000x500")
  ui = UI(root)
  ui.show()
  root.mainloop()

if __name__ == '__main__':
  main()
