from utils.constants import NOTATION_LENGTHS, PITCHES

class ScoreService:
  """Class for editing score"""
  def __init__(self):
    self._score = None

  def get_score(self):
    return self._score

  def set_score(self, score):
    self._score = score

  def add_measure(self):
    self._score.get_staff().add_measure()
  
  def add_note(self, measure_index, length, pitch):
    is_valid_input = True
    measure_index = int(measure_index)
    length = int(length)

    if measure_index < 0 or measure_index >= len(self._score.get_staff().get_measures()):
      print("BAD MEASURE INDEX")
      is_valid_input = False

    if length not in NOTATION_LENGTHS: # 8,4,2
      print("BAD LENGTH INPUT")
      is_valid_input = False

    if pitch not in PITCHES: #  'c4', 'd4', 'e4', 'f4', 'g4', 'a4', 'b4'
      print("BAD PITCH INPUT")
      is_valid_input = False

    if is_valid_input:
      self._score.get_staff().add_note(
        measure_index,
        NOTATION_LENGTHS.index(length),
        PITCHES.index(pitch)
        )

    return is_valid_input

score_service = ScoreService()
