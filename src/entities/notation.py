from utils.constants import NOTATION_LENGTHS

class Notation:
  def __init__(self):
    self._length = None

  def set_length(self, index):
    self._length = NOTATION_LENGTHS[index]

  def __str__(self):
    return 'To string for Notation class'
