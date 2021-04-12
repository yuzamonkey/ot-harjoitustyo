class Clef:
  def __init__(self, clef):
    self._clef = clef

  def get_clef(self):
    return self._clef

  def __str__(self):
    return f'Clef: {self._clef}'
    