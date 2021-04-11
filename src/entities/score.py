class Score:
  """Class for handling a score of music"""
  def __init__(self):
    self._score = None

  def score_is_selected_for_edit(self):
    return self._score != None

  