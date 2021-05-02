import tkinter as tk
from utils.colors import LIGHT_GRAY
from utils.constants import PITCHES, PITCH_POSITIONS_IN_G_CLEF, PITCH_POSITIONS_IN_F_CLEF
from services.score_service import score_service
from PIL import Image, ImageTk

class ScoreView:
  def __init__(self, parent_frame):
    self._frame = parent_frame
    self._title_frame = None
    self._score_frame = None

    self._score = None
    self._clef = ImageTk.PhotoImage(Image.open('./src/utils/images/G-clef.gif').resize((140,230)))
    self._time_signature = ImageTk.PhotoImage(Image.open('./src/utils/images/44.gif').resize((80,175)))
    self._half_note = ImageTk.PhotoImage(Image.open('./src/utils/images/half_note.gif').resize((90,120)))

  def show(self):
    self.update()

  def destroy(self):
    self._frame.destroy()

  def update(self):
    self._score = score_service.get_score()

    if self._title_frame:
      self._title_frame.destroy()
    self._title_frame = tk.Frame(master=self._frame, height=50)
    self._title_frame.pack(fill=tk.X, side=tk.TOP)
    self._title_frame.pack_propagate(0)
    self._show_title()

    if self._score_frame:
      self._score_frame.destroy()
    self._score_frame = tk.Frame(master=self._frame)
    self._score_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
    self._score_frame.columnconfigure([0,1,2], weight=2)
    self._score_frame.rowconfigure([0,1], weight=2)

    self._show_score()

  def _show_title(self):
    score_title = tk.Label(master=self._title_frame, text=self._score.get_title(), pady=20, font=('Arial', 30))
    score_title.pack()

  def _show_score(self):
    canvas = tk.Canvas(master=self._score_frame, width=700, height=1000, confine=True, cursor='circle')

    measure_count = score_service.get_staff_length()

    # Clef
    canvas.create_image(35, 105, image=self._clef, anchor=tk.constants.NW)
    # Time signature
    canvas.create_image(130, 127, image=self._time_signature, anchor=tk.constants.NW)

    notation_position = 200
    notation_gap = 75

    for i in range (measure_count):
      measure = self._score.get_staff().get_measures()[i]
      for notation in measure.get_notations():
        if (notation.is_note()):
          pitch = notation.get_pitch()
          pitch_index = PITCHES.index(pitch)
          if (measure.get_clef().get_clef() == 'G'):
            note_position = PITCH_POSITIONS_IN_G_CLEF[pitch_index]
          elif (measure.get_clef().get_clef() == 'F'):
            note_position = PITCH_POSITIONS_IN_F_CLEF[pitch_index]
          canvas.create_image(notation_position, note_position, image=self._half_note, anchor=tk.constants.NW)
          notation_position += notation_gap
      if i == measure_count-1:
        break
      canvas.create_line(notation_position+25, 150, notation_position+25, 270)
      notation_position += 25

    endline = notation_position + 50
    
    # Padding end
    canvas.create_rectangle(endline, 0, endline+50, 100, outline='white')
    # Staff
    canvas.create_line(50, 150, endline, 150, fill='black')
    canvas.create_line(50, 180, endline, 180, fill='black')
    canvas.create_line(50, 210, endline, 210, fill='black')
    canvas.create_line(50, 240, endline, 240, fill='black')
    canvas.create_line(50, 270, endline, 270, fill='black')
    # Starting diagonal line
    canvas.create_line(50, 150, 50, 270, fill='black')
    # Ending diagonal lines
    canvas.create_line(endline-10, 150, endline-10, 270, fill='black')
    canvas.create_rectangle(endline, 150, endline +10, 270, fill='black')

    # Horizontal scroll
    scroll_x = tk.Scrollbar(self._score_frame, orient="horizontal", command=canvas.xview)
    scroll_x.grid(row=1, column=0, sticky="ews", columnspan=3)

    canvas.configure(xscrollcommand=scroll_x.set)
    canvas.configure(scrollregion=canvas.bbox("all"))

    canvas.grid(row=1, column=0, sticky='esw', columnspan=3)

    # for i in range (0, len(self._score.get_staff().get_measures())):
    #   measure = tk.Label(
    #     master=self._score_frame,
    #     text=f'Measure {i+1}:\n{str(self._score.get_staff().get_measures()[i])}')
    #   measure.grid(row=0, column=i)
