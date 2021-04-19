from entities.staff import Staff

class Score:
  """Class for handling a score of music"""
  def __init__(self, title):
    self._title = title
    self._staff = Staff()

  def get_title(self):
    return self._title

  def set_title(self, title):
    self._title = title

  def get_staff(self):
    return self._staff

  def set_score(self, score):
    pass

  def __str__(self):
    return str(self._staff)
    