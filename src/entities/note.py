from entities.notation import Notation
from utils.constants import PITCHES

class Note(Notation):
  def __init__(self, length_index, pitch_index):
    super().__init__(length_index)
    self._pitch = PITCHES[pitch_index]

  def get_pitch(self):
    return self._pitch

  def set_pitch(self, index):
    self._pitch = PITCHES[index]

  def is_note(self):
    return True

  def __str__(self):
    to_string = f"""
      Note:
      length: {self._length}
      pitch: {self._pitch}
    """
    return to_string
