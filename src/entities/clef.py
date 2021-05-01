from utils.constants import CLEFS

class Clef:
  """Class for getting and setting the clef

  Attributes:
    clef_index: Index of clef defined in utils/constants.py-file
  """
  def __init__(self, clef_index):
    """Constructor for Clef class

    Args:
        clef_index (int): Index of clef defined in utils/constants.py-file
    """
    self._clef = CLEFS[clef_index]

  def get_clef(self):
    """Returns the clef in string format

    Returns:
        str: clef
    """
    return self._clef

  def set_clef(self, clef_index):
    """Sets the clef with clef_index

    Args:
        clef_index (int): Index of clef defined in utils/constants.py-file
    """
    self._clef = CLEFS[clef_index]
    