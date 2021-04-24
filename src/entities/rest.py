from entities.notation import Notation

class Rest(Notation):

  def is_note(self):
    return False

  def __str__(self):
    to_string = f"""
      Rest:
      length: {self._length}
    """
    return to_string
