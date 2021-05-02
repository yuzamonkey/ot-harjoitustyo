from utils.constants import CLEFS, NOTATION_LENGTHS, KEY_SIGNATURES, PITCHES, TIME_SIGNATURES

class ScoreService:
  """Class for editing a score"""
  def __init__(self):
    """Constructor for ScoreService. Current score is set to None
    """
    self._score = None

  def get_score(self):
    """Returns the current score 

    Returns:
        Score: Score that is currently being edited
    """
    return self._score

  def set_score(self, score):
    """Sets the score

    Args:
        score (Score): Sets the current score
    """
    self._score = score

  def get_title(self):
    """Returns the scores title

    Returns:
        str: Current scores title
    """
    return self._score.get_title()

  def set_title(self, title):
    """Sets the title of the current score. Minimum length of the title is 1 and maximum length is 15

    Args:
        title (str): New title of the score
    """
    if len(title) > 0 and len(title) <= 15:
      self._score.set_title(title)
    if len(title) > 15:
      self._score.set_title(title[0:15])

  def get_staff_length(self):
    """Returns the amount of measures in a staff

    Returns:
        int: amount of measures in the scores staff
    """
    return len(self._score.get_staff().get_measures())

  def get_measure_numbers(self):
    """Returns a list of measure numbers

    Returns:
        list: measure numbers]
    """
    numbers = []
    for i in range(self.get_staff_length()):
      numbers.append(i+1)
    return numbers

  def get_notations(self):
    """Returns all the notatios and their measure of the score as a list of strings

    Returns:
        list: Notations of the score
    """
    notations_array = []
    measures = self._score.get_staff().get_measures()
    for i in range (len(measures)):
      notations = measures[i].get_notations()
      for j in range (len(notations)):
        text = f'M{i+1}, N{j+1}:  {str(notations[j])}'
        notations_array.append(text)

    return notations_array

  def get_clef(self):
    """Returns the clef as a string

    Returns:
        str: clef
    """
    return self._score.get_staff().get_measures()[0].get_clef().get_clef()

  def get_key_signature(self):
    """Returns the key signature as a string

    Returns:
        str: key signature
    """
    return self._score.get_staff().get_measures()[0].get_key_signature().get_key_signature()

  def get_time_signature(self):
    """Returns the time signature as a string

    Returns:
        str: time signature
    """
    return self._score.get_staff().get_measures()[0].get_time_signature().get_time_signature()

  def add_measure(self):
    """Adds an empty measure to the scores measures
    """
    self._score.get_staff().add_measure()

  def remove_last_measure(self):
    """Removes the last measure in the score if the score has measures
    """
    if len(self._score.get_staff().get_measures()) > 1:
      self._score.get_staff().remove_last_measure()

  def add_note(self, measure, length, pitch):
    """Adds a note to the score. Input is validated.

    Args:
        measure (int): measure where the note is added
        length (int): length of the note
        pitch (string): pitch of the note

    Returns:
        bool: Returns True if the input is valid and the note can be added
    """
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
    """Adds a rest to the score. Input is validated.

    Args:
        measure (int): measure where the rest is added
        length (int): length of the rest

    Returns:
        bool: Returns True if the input is valid and the rest can be added
    """
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

  def remove_notation(self, measure_index, notation_index):
    """Removes either a rest or a note

    Args:
        measure_index (int): Index of the measure where the notation is removed from
        notation_index (int): Index of the notation in the measure
    """
    measure = self._score.get_staff().get_measures()[measure_index]
    measure.remove_notation(notation_index)

  def change_clef(self, clef):
    """Change the clef of the score. Input is validated.

    Args:
        clef (str): Clef in string format

    Returns:
        bool: Returns True if the input is valid and the clef can be changed
    """
    is_valid_input = True
    if clef not in CLEFS:
      is_valid_input = False

    if is_valid_input:
      self._score.get_staff().change_clef(CLEFS.index(clef))

    return is_valid_input

  def change_key(self, key):
    """Change the key signature of the score. Input is validated.

    Args:
        key (str): Key signature in string format

    Returns:
        bool: Returns True if the input is valid and the key signature can be changed
    """
    is_valid_input = True
    if key not in KEY_SIGNATURES:
      is_valid_input = False

    if is_valid_input:
      self._score.get_staff().change_key(KEY_SIGNATURES.index(key))

    return is_valid_input

  def change_time_signature(self, time):
    """Change the time signature of the score. Input is validated.

    Args:
        time (str): Time signature in string format

    Returns:
        bool: Returns True if the input is valid and the time signature can be changed
    """
    is_valid_input = True
    if time not in TIME_SIGNATURES:
      is_valid_input = False

    if is_valid_input:
      self._score.get_staff().change_time_signature(TIME_SIGNATURES.index(time))

    return is_valid_input

score_service = ScoreService()
