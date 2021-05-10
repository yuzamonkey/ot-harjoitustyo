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
    
    self._clef = None
    self._time_signature = None

    self._sixteenth_note = ImageTk.PhotoImage(Image.open('./src/utils/images/sixteenth_note.gif').resize((90,120)))
    self._eight_note = ImageTk.PhotoImage(Image.open('./src/utils/images/eight_note.gif').resize((90,120)))
    self._quarter_note = ImageTk.PhotoImage(Image.open('./src/utils/images/quarter_note.gif').resize((90,120)))
    self._half_note = ImageTk.PhotoImage(Image.open('./src/utils/images/half_note.gif').resize((90,120)))
    
    self._sixteenth_rest = ImageTk.PhotoImage(Image.open('./src/utils/images/sixteenth_rest.gif').resize((50,100)))
    self._eight_rest = ImageTk.PhotoImage(Image.open('./src/utils/images/eight_rest.gif').resize((50,100)))
    self._quarter_rest = ImageTk.PhotoImage(Image.open('./src/utils/images/quarter_rest.gif').resize((50,100)))
    self._half_rest = ImageTk.PhotoImage(Image.open('./src/utils/images/half_rest.gif').resize((50,100)))

    self._opened_first_time = True

  def show(self):
    self.update()

  def destroy(self):
    self._frame.destroy()

  def update(self):
    self._score = score_service.get_score()
    clef = self._score.get_staff().get_measures()[0].get_clef().get_clef()
    if clef == 'G':
      self._clef = ImageTk.PhotoImage(Image.open('./src/utils/images/G-clef.gif').resize((140,230)))
    elif clef == 'F':
      self._clef = ImageTk.PhotoImage(Image.open('./src/utils/images/F-clef.gif').resize((110,200)))

    time_signature = self._score.get_staff().get_measures()[0].get_time_signature().get_time_signature()
    if time_signature == '2/4':
      self._time_signature = ImageTk.PhotoImage(Image.open('./src/utils/images/24.gif').resize((70,150)))
    elif time_signature == '3/4':
      self._time_signature = ImageTk.PhotoImage(Image.open('./src/utils/images/34.gif').resize((70,150)))
    elif time_signature == '4/4':
      self._time_signature = ImageTk.PhotoImage(Image.open('./src/utils/images/44.gif').resize((70,150)))
    elif time_signature == '6/8':
      self._time_signature = ImageTk.PhotoImage(Image.open('./src/utils/images/68.gif').resize((70,150)))

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
    canvas = tk.Canvas(master=self._score_frame, width=700, height=1000, confine=True)

    measure_count = score_service.get_staff_length()

    # Clef
    canvas.create_image(50, 105, image=self._clef, anchor=tk.constants.NW)
    # Time signature
    canvas.create_image(150, 140, image=self._time_signature, anchor=tk.constants.NW)

    notation_position = 200
    notation_gap = 75

    for i in range (measure_count):
      measure = self._score.get_staff().get_measures()[i]
      for notation in measure.get_notations():
        length = notation.get_length()

        if (notation.is_note()): #note
          pitch = notation.get_pitch()
          pitch_index = PITCHES.index(pitch)
          if (measure.get_clef().get_clef() == 'G'):
            note_position = PITCH_POSITIONS_IN_G_CLEF[pitch_index]
          elif (measure.get_clef().get_clef() == 'F'):
            note_position = PITCH_POSITIONS_IN_F_CLEF[pitch_index]
          if length == 2:
            canvas.create_image(notation_position, note_position, image=self._half_note, anchor=tk.constants.NW)
          elif length == 4:
            canvas.create_image(notation_position, note_position, image=self._quarter_note, anchor=tk.constants.NW)
          elif length == 8:
            canvas.create_image(notation_position, note_position, image=self._eight_note, anchor=tk.constants.NW)
          elif length == 16:
            canvas.create_image(notation_position, note_position, image=self._sixteenth_note, anchor=tk.constants.NW)

          if note_position <= 20: # add top ledger lines
            ledger_line_position = 120
            while (ledger_line_position - 100 >= note_position):
              canvas.create_line(notation_position+10, ledger_line_position, notation_position+65, ledger_line_position, fill='black')
              ledger_line_position -= 30

          if note_position >= 200: # add bottom ledger lines
            ledger_line_position = 300
            while (ledger_line_position - 100 <= note_position):
              canvas.create_line(notation_position+10, ledger_line_position, notation_position+65, ledger_line_position, fill='black')
              ledger_line_position += 30

        else: #rest
          if length == 2:
            canvas.create_image(notation_position, 152, image=self._half_rest, anchor=tk.constants.NW)
          elif length == 4:
            canvas.create_image(notation_position, 152, image=self._quarter_rest, anchor=tk.constants.NW)
          elif length == 8:
            canvas.create_image(notation_position, 152, image=self._eight_rest, anchor=tk.constants.NW)
          elif length == 16:
            canvas.create_image(notation_position, 152, image=self._sixteenth_rest, anchor=tk.constants.NW)
        
        notation_position += notation_gap
      if i == measure_count-1:
        break
      canvas.create_line(notation_position+25, 150, notation_position+25, 270)
      notation_position += 25

    endline = notation_position + 50

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
    canvas.create_rectangle(endline, 150, endline+10, 270, fill='black')

    # Horizontal scroll
    scroll_x = tk.Scrollbar(self._score_frame, orient="horizontal", command=canvas.xview)
    scroll_x.grid(row=1, column=0, sticky="ews", columnspan=3)

    canvas.configure(xscrollcommand=scroll_x.set)
    canvas.configure(scrollregion=canvas.bbox("all"))
    
    if not self._opened_first_time:
      canvas.xview_moveto(1) #position scroll to end
    self._opened_first_time = False

    canvas.grid(row=1, column=0, sticky='esw', columnspan=3, padx=25)
