from utils.constants import CLEFS, KEY_SIGNATURES, TIME_SIGNATURES
from entities.measure import Measure

class Staff:
  """Class for handling the staff"""
  def __init__(self):
    self._measures = [
      Measure(0, 1, 2),
      Measure(0, 1, 2),
      Measure(0, 1, 2)
    ]

  def get_measures(self):
    return self._measures

  def add_measure(self):
    last_index = len(self._measures)-1
    self._measures.append(
      Measure(
        CLEFS.index(str(self._measures[last_index].get_clef())),
        KEY_SIGNATURES.index(str(self._measures[last_index].get_key_signature())),
        TIME_SIGNATURES.index(str(self._measures[last_index].get_time_signature())),
      )
    )

  def add_note(self, measure_index, length_index, pitch_index):
    self._measures[measure_index].add_note(length_index, pitch_index)

  def add_rest(self, measure_index, length_index):
    self._measures[measure_index].add_rest(length_index)

  def change_clef(self, clef_index):
    for measure in self._measures:
      measure.get_clef().set_clef(clef_index)

  def change_key(self, key_index):
    for measure in self._measures:
      measure.get_key_signature().set_key_signature(key_index)
  
  def change_time_signature(self, time_signature_index):
    for measure in self._measures:
      measure.get_time_signature().set_time_signature(time_signature_index)

  def __str__(self):
    to_string = ""
    for measure in self._measures:
      to_string += f'{str(measure)} \n'
    return to_string
    