from entities.bar import Bar

class Staff:
  """Class for handling the staff"""
  def __init__(self):
    self._bars = [Bar(), Bar(), Bar()]

  def add_bar(self):
    self._bars.append(Bar())

  def __str__(self):
    return 'toString method for class Staff'
    