from utils.constants import CLEFS, NOTATION_LENGTHS, KEY_SIGNATURES, PITCHES

class ScoreService:
  """Class for editing score"""
  def __init__(self):
    self._score = None

  def get_score(self):
    return self._score

  def set_score(self, score):
    self._score = score

  def get_length(self):
    return len(self._score.get_staff().get_measures())

  def get_measure_numbers(self):
    numbers = []
    for i in range(self.get_length()):
      numbers.append(i+1)
    return numbers

  def add_measure(self):
    self._score.get_staff().add_measure()

  def add_note(self, measure, length, pitch):
    is_valid_input = True
    measure_index = int(measure)-1
    length = int(length)

    if measure_index < 0 or measure_index >= self.get_length():
      print("BAD MEASURE INDEX")
      is_valid_input = False

    if length not in NOTATION_LENGTHS:
      print("BAD LENGTH INPUT")
      is_valid_input = False

    if pitch not in PITCHES:
      print("BAD PITCH INPUT")
      is_valid_input = False

    if is_valid_input:
      self._score.get_staff().add_note(
        measure_index,
        NOTATION_LENGTHS.index(length),
        PITCHES.index(pitch)
        )

    return is_valid_input

  def add_rest(self, measure, length):
    is_valid_input = True
    measure_index = int(measure)-1
    length = int(length)
    if measure_index < 0 or measure_index >= self.get_length():
      print("BAD MEASURE INDEX")
      is_valid_input = False

    if length not in NOTATION_LENGTHS:
      print("BAD LENGTH INPUT")
      is_valid_input = False

    if is_valid_input:
      self._score.get_staff().add_rest(
        measure_index,
        NOTATION_LENGTHS.index(length)
        )

    return is_valid_input

  def change_clef(self, clef):
    is_valid_input = True
    if clef not in CLEFS:
      is_valid_input = False

    if is_valid_input:
      self._score.get_staff().change_clef(CLEFS.index(clef))

    return is_valid_input

  def change_key(self, key):
    is_valid_input = True
    if key not in KEY_SIGNATURES:
      is_valid_input = False

    if is_valid_input:
      self._score.get_staff().change_key(KEY_SIGNATURES.index(key))

    return is_valid_input

score_service = ScoreService()
