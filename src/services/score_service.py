from utils.constants import CLEFS, NOTATION_LENGTHS, KEY_SIGNATURES, PITCHES, TIME_SIGNATURES

class ScoreService:
  """Class for editing score"""
  def __init__(self):
    self._score = None

  def get_score(self):
    return self._score

  def set_score(self, score):
    self._score = score

  def get_title(self):
    return self._score.get_title()

  def set_title(self, title):
    self._score.set_title(title)

  def get_staff_length(self):
    return len(self._score.get_staff().get_measures())

  def get_measure_numbers(self):
    numbers = []
    for i in range(self.get_staff_length()):
      numbers.append(i+1)
    return numbers

  def get_clef(self):
    return self._score.get_staff().get_measures()[0].get_clef().get_clef()

  def get_key_signature(self):
    return self._score.get_staff().get_measures()[0].get_key_signature().get_key_signature()

  def get_time_signature(self):
    return self._score.get_staff().get_measures()[0].get_time_signature().get_time_signature()

  def add_measure(self):
    self._score.get_staff().add_measure()

  def remove_last_measure(self):
    if self._score.get_staff().get_measures():
      self._score.get_staff().remove_last_measure()

  def add_note(self, measure, length, pitch):
    is_valid_input = True
    measure_index = int(measure)-1
    length = int(length)

    if measure_index < 0 or measure_index >= self.get_staff_length():
      print("BAD MEASURE INDEX")
      is_valid_input = False

    if length not in NOTATION_LENGTHS:
      print("BAD LENGTH INPUT")
      is_valid_input = False

    if pitch not in PITCHES:
      print("BAD PITCH INPUT")
      is_valid_input = False

    if not self._score.get_staff().get_measures()[measure_index].measure_has_space(length):
      print("MEASURE DOESN'T HAVE SPACE")
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
    if measure_index < 0 or measure_index >= self.get_staff_length():
      print("BAD MEASURE INDEX")
      is_valid_input = False

    if length not in NOTATION_LENGTHS:
      print("BAD LENGTH INPUT")
      is_valid_input = False

    if not self._score.get_staff().get_measures()[measure_index].measure_has_space(length):
      print("MEASURE DOESN'T HAVE SPACE")
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

  def change_time_signature(self, time):
    is_valid_input = True
    if time not in TIME_SIGNATURES:
      is_valid_input = False

    if is_valid_input:
      self._score.get_staff().change_time_signature(TIME_SIGNATURES.index(time))

    return is_valid_input

score_service = ScoreService()
