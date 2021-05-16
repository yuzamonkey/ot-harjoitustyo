from entities.notation import Notation

class Rest(Notation):
  """Class for Rest. This class inherits Notation class

  Attributes:
      Notation (length_index): Index of notation length defined in utils/constants.py-file
  """
  def __str__(self):
    """Returns a string representation of Rest class

    Returns:
      str: class name and length
    """
    to_string = f"""
      Rest
      length: {self._length}
    """
    return to_string
