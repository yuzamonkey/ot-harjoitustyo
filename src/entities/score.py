from entities.staff import Staff

class Score:
  """Class for handling a score of music"""
  def __init__(self, title):
    self._staff = None
    self._title = title

  def score_is_selected_for_edit(self):
    return self._staff != None

  def set_name(self, title):
    self._title = title

  def set_score(self, score):
    if score:
      self._staff = score.staff
    else:
      self._score = Staff()
    
  def __str__(self):
    return f'toString method for class Score: title {self._title}'