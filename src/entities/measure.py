from entities.clef import Clef
from entities.key_signature import KeySignature
from entities.time_signature import TimeSignature
from entities.note import Note
from entities.rest import Rest

class Measure:
  """Class for handling a measure in the measures list. The list is defined in the Staff class.

  Attributes:
    clef_index (int): Index of clef defined in utils/constants.py-file
    key_signature_index (int): Index of key signature defined in utils/constants.py-file
    time_signature_index (int): Index of time signature defined in utils/constants.py-file
  """
  def __init__(self, clef_index, key_signature_index, time_signature_index):
    """Constructor for Measure class

    Args:
      clef_index (int): Index of clef defined in utils/constants.py-file
      key_signature_index (int): Index of key signature defined in utils/constants.py-file
      time_signature_index (int): Index of time signature defined in utils/constants.py-file
    """
    self._clef = Clef(clef_index)
    self._key_signature = KeySignature(key_signature_index)
    self._time_signature = TimeSignature(time_signature_index)
    self._notations = []

  def get_clef(self):
    """Returns the clef object of the measure

    Returns:
        Clef: clef object
    """
    return self._clef

  def get_key_signature(self):
    """Returns the key signature object of the measure

    Returns:
        KeySignature: key signature object
    """
    return self._key_signature

  def get_time_signature(self):
    """Returns the time signature object of the measure

    Returns:
        TimeSignature: time signature object
    """
    return self._time_signature

  def get_notations(self):
    """Returns the list of notations

    Returns:
        list: list of notations
    """
    return self._notations

  def _space_taken(self):
    """Returns how much space is taken by the notations in the measure

    Returns:
        float: space taken relative to beat unit
    """
    space_taken = 0.0
    beat_unit = self._time_signature.get_beat_unit()
    for notation in self._notations:
      notation_length = float(notation.get_length())
      space_taken += beat_unit / notation_length
    return space_taken

  def measure_has_space(self, input_length):
    """Returns true if a measure has space for a notation

    Args:
        input_length (int): Index of notation length defined in utils/constants.py-file

    Returns:
        bool: returns true if the measure can fit a notation
    """
    space_taken = self._space_taken()
    beats_per_measure = self._time_signature.get_beats_per_measure()
    beat_unit = self._time_signature.get_beat_unit()

    takes_space = space_taken + (beat_unit / float(input_length))
    return takes_space <= beats_per_measure

  def measure_is_full(self):
    """Returns true if measure has no more space for notations

    Returns:
        bool: returns true if measure has no more space for notations
    """
    space_taken = self._space_taken()
    beats_per_measure = self._time_signature.get_beats_per_measure()
    beat_unit = self._time_signature.get_beat_unit()

    return space_taken >= beats_per_measure

  def remove_overflown_notations(self):
    """Removes notations from the end while measure has space or has exact amount of notations
    """
    space_taken = self._space_taken()
    beats_per_measure = self._time_signature.get_beats_per_measure()
    beat_unit = self._time_signature.get_beat_unit()

    while space_taken > beats_per_measure:
      self.remove_notation(len(self._notations) - 1)
      space_taken = self._space_taken()

  def add_note(self, length_index, pitch_index):
    """Adds a note to the list of notations

    Args:
        length_index (int): Index of notation length defined in utils/constants.py-file
        pitch_index (int): Index of pitch defined in utils/constants.py-file
    """
    self._notations.append(Note(length_index, pitch_index))

  def add_rest(self, length_index):
    """Adds a rest to the list of notations

    Args:
        length_index (int): Index of notation length defined in utils/constants.py-file
    """
    self._notations.append(Rest(length_index))

  def remove_notation(self, notation_index):
    """Removes a notation

    Args:
        notation_index (int): Removes the given index from the notations list
    """
    self._notations.pop(notation_index)

  def __str__(self):
    """Returns a string representation of the Measure class

    Returns:
        str: Clef, key signature and time signature of the measure. Also the notations from the notations list.
    """
    to_string = f"""
      Clef: {self._clef.get_clef()}
      Key: {self._key_signature.get_key_signature()}
      Time: {self._time_signature.get_time_signature()}
    """
    notations_to_string = 'Notations: [\n'
    for notation in self._notations:
      notations_to_string += f'{notation}\n'
    notations_to_string += "]"
    if self.measure_is_full():
      return f'(full) {to_string} {notations_to_string}'
    return f'{to_string} {notations_to_string}'
