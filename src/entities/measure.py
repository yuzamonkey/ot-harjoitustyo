from entities.clef import Clef
from entities.key_signature import KeySignature
from entities.time_signature import TimeSignature
from entities.note import Note
from entities.rest import Rest
from utils.constants import NOTATION_LENGTHS

class Measure:
  def __init__(self, clef_index, key_signature_index, time_signature_index):
    self._clef = Clef(clef_index)
    self._key_signature = KeySignature(key_signature_index)
    self._time_signature = TimeSignature(time_signature_index)
    self._notations = []

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

  def get_time_signature_beat(self):
    return float(self.get_time_signature().get_time_signature()[-1:])

  def measure_has_space(self, input_length):
    space_taken = 0.0
    time_signature_beat = self.get_time_signature_beat()
    for notation in self._notations:
      notation_length = float(notation.get_length())
      space_taken += time_signature_beat / notation_length 
    
    sum = space_taken + (time_signature_beat / float(input_length))
    return sum <= time_signature_beat

  def add_note(self, length_index, pitch_index):
    self._notations.append(Note(length_index, pitch_index))

  def add_rest(self, length_index):
    self._notations.append(Rest(length_index))

  def __str__(self):
    to_string = f"""
      Clef: {self._clef}
      Key: {self._key_signature}
      Time: {self._time_signature}
    """
    notations_to_string = 'Notations: [\n'
    for notation in self._notations:
      notations_to_string += f'{notation}\n'
    notations_to_string += "]"
    return f'{to_string} {notations_to_string}'
