from entities.notation import Notation

pitches = [
  'c4', 'd4', 'e4', 'f4', 'g4', 'a4', 'b4'
]

class Note(Notation):
  def __init__(self):
    super().__init__()
    self._pitch = pitches[0]

  def set_pitch(self, index):
    self._pitch = pitches[index]

  def __str__(self):
    to_string = f"""
      Note:
      length: {self._length}
      pitch: {self._pitch}
    """
    return to_string
