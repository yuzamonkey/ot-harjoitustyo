from entities.clef import Clef
from entities.key_signature import KeySignature
from entities.time_signature import TimeSignature

class Measure:
  def __init__(self):
    self._clef = Clef('G')
    self._key_signature = KeySignature('C')
    self._time_signature = TimeSignature('44')
    self._notations = []

  def set_clef(self, clef):
    self._clef = Clef(clef)

  def set_key_signature(self, key_signature):
    self._key_signature = KeySignature(key_signature)

  def set_time_signature(self, time_signature):
    self._time_signature = TimeSignature(time_signature)

  def add_note(self):
    pass

  def add_rest(self):
    pass

  def __str__(self):
    return 'ToString method for class Measure'
