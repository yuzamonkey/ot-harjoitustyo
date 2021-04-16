from utils.constants import CLEFS, KEY_SIGNATURES, TIME_SIGNATURES
from entities.measure import Measure

class Staff:
  """Class for handling the staff"""
  def __init__(self):
    self._measures = [
      Measure(CLEFS[0], KEY_SIGNATURES[1], TIME_SIGNATURES[2]),
      Measure(CLEFS[0], KEY_SIGNATURES[1], TIME_SIGNATURES[2]),
      Measure(CLEFS[0], KEY_SIGNATURES[1], TIME_SIGNATURES[2])
    ]

  def get_measures(self):
    return self._measures

  def add_measure(self):
    last_index = len(self._measures)-1
    self._measures.append(
      Measure(
        str(self._measures[last_index].get_clef()),
        str(self._measures[last_index].get_key_signature()),
        str(self._measures[last_index].get_time_signature()),
      )
    )

  def __str__(self):
    to_string = ""
    for measure in self._measures:
      to_string += f'{str(measure)} \n'
    return to_string
    