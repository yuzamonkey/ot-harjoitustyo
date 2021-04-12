from entities.staff import Staff

class Score:
  """Class for handling a score of music"""
  def __init__(self, title):
    self._title = title
    self._staff = Staff()

  def get_name(self):
    return self._title

  def set_name(self, title):
    self._title = title

  def set_score(self, score):
    pass
    
  def __str__(self):
    return f'Score title: {self._title}'