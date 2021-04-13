from entities.measure import Measure

class Staff:
  """Class for handling the staff"""
  def __init__(self):
    self._measures = [Measure(), Measure(), Measure()]

  def add_measure(self):
    self._measures.append(Measure())

  def __str__(self):
    to_string = ""
    for measure in self._measures:
      to_string += f'{str(measure)} | '
    return to_string
    