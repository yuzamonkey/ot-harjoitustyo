class ScoreService:
  """Class for editing score"""
  def __init__(self):
    self._score = None

  def get_score(self):
    return self._score

  def set_score(self, score):
    self._score = score

  def add_measure(self):
    self._score.get_staff().add_measure()

score_service = ScoreService()
