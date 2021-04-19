from utils.constants import CLEFS

class Clef:
  def __init__(self, clef_index):
    self._clef = CLEFS[clef_index]

  def get_clef(self):
    return self._clef

  def set_clef(self, clef_index):
    self._clef = CLEFS[clef_index]

  def __str__(self):
    return self._clef
    