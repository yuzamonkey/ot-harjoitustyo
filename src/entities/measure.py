from entities.clef import Clef
from entities.key_signature import KeySignature
from entities.time_signature import TimeSignature
# from entities.note import Note
# from entities.rest import Rest

class Measure:
  def __init__(self, clef, key_signature, time_signature):
    self._clef = Clef(clef)
    self._key_signature = KeySignature(key_signature)
    self._time_signature = TimeSignature(time_signature)
    self._notations = []

  def set_clef(self, clef):
    self._clef = Clef(clef)

  def get_clef(self):
    return self._clef

  def set_key_signature(self, key_signature):
    self._key_signature = KeySignature(key_signature)

  def get_key_signature(self):
    return self._key_signature

  def set_time_signature(self, time_signature):
    self._time_signature = TimeSignature(time_signature)

  def get_time_signature(self):
    return self._time_signature

  def add_note(self):
    pass

  def add_rest(self):
    pass

  def __str__(self):
    to_string = f"""
      {self._clef}
      {self._key_signature}
      {self._time_signature}
    """
    notations_to_string = 'Notations: [ '
    for notation in self._notations:
      notations_to_string += f'{str(notation)}'
    notations_to_string += " ]"
    return f'Measure: {to_string} {notations_to_string} \n______________'
