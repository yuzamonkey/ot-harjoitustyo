from utils.constants import CLEFS, KEY_SIGNATURES, TIME_SIGNATURES
from entities.measure import Measure

class Staff:
  """Class for handling the staff of the score

  Attributes:
    measures: The default list of measures is three measures with G clef, 4/4 time signature and C/a key signature
  """
  def __init__(self):
    """Constructor for Staff class

    Args:
    """
    self._measures = [
      Measure(0, 1, 2),
      Measure(0, 1, 2),
      Measure(0, 1, 2)
    ]

  def get_measures(self):
    """Returns the list of measures

    Returns:
        list: list of measures
    """
    return self._measures

  def add_measure(self):
    """Adds an empty measure in the measures list

    Args:
    """
    last_index = len(self._measures)-1
    self._measures.append(
      Measure(
        CLEFS.index(self._measures[last_index].get_clef().get_clef()),
        KEY_SIGNATURES.index(self._measures[last_index].get_key_signature().get_key_signature()),
        TIME_SIGNATURES.index(self._measures[last_index].get_time_signature().get_time_signature()),
      )
    )

  def remove_last_measure(self):
    """Removes the last measure in the measures list

    Args:
    """
    self._measures.pop()

  def add_note(self, measure_index, length_index, pitch_index):
    """Adds a note in a measure in the measures list

    Args:
      measure_index (int): Index of the measure
      length_index (int): Index of notation length defined in utils/constants.py-file
      pitch_index (int): Index of pitch defined in utils/constants.py-file
    """
    self._measures[measure_index].add_note(length_index, pitch_index)

  def add_rest(self, measure_index, length_index):
    """Adds a rest in a measure in the measures list

    Args:
      measure_index: Index of the measure
      length_index: Index of notation length defined in utils/constants.py-file
    """
    self._measures[measure_index].add_rest(length_index)

  def change_clef(self, clef_index):
    """Changes the clef of all the measures in the measures list

    Args:
        clef_index (int): Index of clef defined in utils/constants.py-file
    """
    for measure in self._measures:
      measure.get_clef().set_clef(clef_index)

  def change_key(self, key_signature_index):
    """Changes the key signature of all the measures in the measures list

    Args:
        key_signature_index (int): Index of key signature defined in utils/constants.py-file
    """
    for measure in self._measures:
      measure.get_key_signature().set_key_signature(key_signature_index)

  def change_time_signature(self, time_signature_index):
    """Changes the time signature of all the measures in the measures list

    Args:
        time_signature_index (int): Index of time signature defined in utils/constants.py-file
    """
    for measure in self._measures:
      measure.get_time_signature().set_time_signature(time_signature_index)
      measure.remove_overflown_notations()

  def __str__(self):
    """Returns a string representation of the Staff class

    Returns:
        str: each measure of the staff
    """
    to_string = ""
    for measure in self._measures:
      to_string += f'{str(measure)} \n'
    return to_string
    