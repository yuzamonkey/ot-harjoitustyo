from entities.notation import Notation
from utils.constants import PITCHES

class Note(Notation):
  """Class for Note. This class inherits Notation class

  Attributes:
      Notation (length_index): Index of notation length defined in utils/constants.py-file
      pitch_index (int): Index of pitch defined in utils/constants.py-file
  """
  def __init__(self, length_index, pitch_index):
    """Constructor for Note class

    Args:
      length_index (int): Index of notation length defined in utils/constants.py-file
      pitch_index (int): Index of pitch defined in utils/constants.py-file
    """
    super().__init__(length_index)
    self._pitch = PITCHES[pitch_index]

  def get_pitch(self):
    """Return the pitch in string format

    Returns:
        str: pitch
    """
    return self._pitch

  def get_note(self):
    """Return the note in string format

    Returns:
        str: note
    """
    return self._pitch[0:1]

  def get_pitch_class(self):
    """Return the pitch class in string format

    Returns:
        str: pitch class
    """
    return self._pitch[1:2]

  def set_pitch(self, index):
    """Sets the pitch with pitch_index

    Args:
        pitch_index (int): Index of pitch defined in utils/constants.py-file
    """
    self._pitch = PITCHES[index]

  def is_note(self):
    """Returns true if the notation is a note and false if the notation is a rest

    Returns:
        bool: returns True
    """
    return True
