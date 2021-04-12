from entities.measure import Measure

class Staff:
  """Class for handling the staff"""
  def __init__(self):
    self._measures = [Measure(), Measure(), Measure()]

  def add_measure(self):
    self._measures.append(Measure())

  def __str__(self):
    return 'toString method for class Staff'
    