import tkinter as tk
from utils.colors import LIGHT_GRAY
from services.score_service import score_service
from PIL import Image, ImageTk

class ScoreView:
  def __init__(self, parent_frame):
    self._score = score_service.get_score()
    self._frame = parent_frame
    self._title_frame = None
    self._score_frame = None

    self._clef = ImageTk.PhotoImage(Image.open('./src/utils/images/G-clef.gif').resize((120,200)))
    self._time_signature = ImageTk.PhotoImage(Image.open('./src/utils/images/44.gif').resize((70,145)))
    self._quartet_note = ImageTk.PhotoImage(Image.open('./src/utils/images/Quartet_note.gif').resize((70,145)))

  def show(self):
    self.update()
    self._show_title()
    self._show_score()

  def destroy(self):
    self._frame.destroy()

  def update(self):
    self._score = score_service.get_score()

    if self._title_frame:
      self._title_frame.destroy()
    self._title_frame = tk.Frame(master=self._frame, height=50, bg='red')
    self._title_frame.pack(fill=tk.X, side=tk.TOP)
    self._title_frame.pack_propagate(0)
    self._show_title()

    if self._score_frame:
      self._score_frame.destroy()
    self._score_frame = tk.Frame(master=self._frame, bg='green')
    self._score_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
    self._score_frame.columnconfigure([0,1,2], weight=2)
    self._score_frame.rowconfigure([0,1,2], weight=2)

    self._show_score()

  def _show_title(self):
    score_title = tk.Label(master=self._title_frame, text=self._score.get_title(), pady=20)
    score_title.pack()

  def _show_score(self):
    measure_count = score_service.get_staff_length()
    endline = measure_count * 500

    canvas = tk.Canvas(master=self._score_frame, width=700, height=300, confine=True, cursor='circle')
    
    # Padding top
    canvas.create_rectangle(0, 0, endline, 50, outline='white')
    # Padding end
    canvas.create_rectangle(endline, 0, endline+50, 100, outline='white')
    # Staff
    canvas.create_line(50, 125, endline, 125, fill='black')
    canvas.create_line(50, 150, endline, 150, fill='black')
    canvas.create_line(50, 175, endline, 175, fill='black')
    canvas.create_line(50, 200, endline, 200, fill='black')
    canvas.create_line(50, 225, endline, 225, fill='black')
    # Starting diagonal line
    canvas.create_line(50, 125, 50, 225, fill='black')
    # Ending diagonal lines
    canvas.create_line(endline-10, 125, endline-10, 225, fill='black')
    canvas.create_rectangle(endline, 125, endline+10, 225, fill='black')

    # Clef
    canvas.create_image(35, 80, image=self._clef, anchor=tk.constants.NW)
    # Time signature
    canvas.create_image(120, 105, image=self._time_signature, anchor=tk.constants.NW)

    # Bar lines
    bar_line_position = 100 + endline / measure_count
    bar_line_width = (endline - 100) / measure_count

    for i in range (measure_count-1):
      canvas.create_line(bar_line_position, 125, bar_line_position, 225)
      bar_line_position += bar_line_width




    # Horizontal scroll
    scroll_x = tk.Scrollbar(self._score_frame, orient="horizontal", command=canvas.xview)
    scroll_x.grid(row=1, column=0, sticky="ews", columnspan=3)

    canvas.configure(xscrollcommand=scroll_x.set)
    canvas.configure(scrollregion=canvas.bbox("all"))

    canvas.grid(row=1, column=0, sticky='nesw', columnspan=3)


    
    # for i in range (0, len(self._score.get_staff().get_measures())):
    #   measure = tk.Label(
    #     master=self._score_frame,
    #     text=f'Measure {i+1}:\n{str(self._score.get_staff().get_measures()[i])}')
    #   measure.grid(row=0, column=i)
