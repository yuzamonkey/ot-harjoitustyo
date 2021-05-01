from utils.constants import NOTATION_LENGTHS

class Notation:
  """Class for Notations. Classes Note and Rest inherit this class

    Attributes:
      length_index: Index of notation length defined in utils/constants.py-file
  """
  def __init__(self, length_index):
    """Constructor for Notation-class

    Args:
        length_index (int): Index of notation length defined in utils/constants.py-file
    """
    self._length = NOTATION_LENGTHS[length_index]

  def get_length(self):
    """Return the notation length in integer format

    Returns:
        int: Notation length
    """
    return self._length

  def set_length(self, length_index):
    """Sets the notation length with length_index

    Args:
        length_index (int): Index of notation length defined in utils/constants.py-file
    """
    self._length = NOTATION_LENGTHS[length_index]

  def is_note(self):
    """Returns true if the notation is a note and false if the notation is a rest

    Returns:
        bool: Notation is note
    """
    return False
