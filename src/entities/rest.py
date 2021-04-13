from entities.notation import Notation

class Rest(Notation):
  def __init__(self):
    super().__init__()

  def __str__(self):
    to_string = f"""
      Rest:
      length: {self._length}
    """
    return to_string
