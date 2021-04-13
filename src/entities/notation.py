
lengths = [8, 4, 2, 1]

class Notation:
  def __init__(self):
    self._length = lengths[1]

  def set_length(self, index):
    self._length = lengths[index]

  def __str__(self):
    return 'To string for Notation class'
