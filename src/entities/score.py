from entities.staff import Staff

class Score:
  """Class for handling a score of music"""
  def __init__(self):
    self._staff = None
    #name

  def score_is_selected_for_edit(self):
    return self._staff != None

  def set_score(self, score):
    if score:
      self._staff = score.staff
    else:
      self._score = Staff()
    
  def __str__(self):
    return 'toString method for class Score'