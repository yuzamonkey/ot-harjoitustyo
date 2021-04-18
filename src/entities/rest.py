from entities.notation import Notation

class Rest():
  def __init__(self, length_index):
    super().__init__(length_index)

  def __str__(self):
    to_string = f"""
      Rest:
      length: {self._length}
    """
    return to_string
