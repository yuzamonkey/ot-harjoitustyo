from entities.clef import Clef
from entities.key_signature import KeySignature
from entities.time_signature import TimeSignature
from entities.notation import Notation

class Bar:
  def __init__(self):
    self._clef = Clef('G')
    self._key_signature = KeySignature('C')
    self._time_signature = TimeSignature('44')
    self._notations = []

  def __str__(self):
    return 'ToString method for class Bar'