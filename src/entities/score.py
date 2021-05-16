from entities.staff import Staff

class Score:
  """Class for handling the Score

  Attributes:
    title (string): Title of the score
    staff (Staff): Staff of the score
    tempo (int): Default tempo is 100 bpm
  """
  def __init__(self, title):
    """Constructor for Score class

    Args:
        title (string): Title of the score
    """
    self._title = title
    self._staff = Staff()
    self._tempo = 100

  def get_title(self):
    """Returns the title of the score

    Returns:
        str: Title of the score
    """
    return self._title

  def set_title(self, title):
    """Sets the title of the score

    Args:
        title (str): Set title of the score
    """
    self._title = title

  def get_staff(self):
    """Returns the staff of the score

    Returns:
        Staff: Staff of the score
    """
    return self._staff

  def get_tempo(self):
    """Returns the tempo of the score

    Returns:
        int: Returns the tempo
    """
    return self._tempo

  def set_tempo(self, tempo):
    """Sets the tempo of the score

    Args:
        tempo (int): Set the tempo
    """
    self._tempo = tempo
