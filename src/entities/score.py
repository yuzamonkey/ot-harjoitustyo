from entities.staff import Staff

class Score:
  """Class for handling a score of music"""
  def __init__(self, title):
    self._title = title
    self._staff = Staff()
    self._tempo = 100

  def get_title(self):
    return self._title

  def set_title(self, title):
    self._title = title

  def get_staff(self):
    return self._staff

  def get_tempo(self):
    return self._tempo

  def set_tempo(self, tempo):
    self._tempo = tempo

  def __str__(self):
    return str(self._staff)
    