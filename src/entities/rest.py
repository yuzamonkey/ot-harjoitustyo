from entities.notation import Notation

class Rest(Notation):

  def __str__(self):
    to_string = f"""
      Rest:
      length: {self._length}
    """
    return to_string
