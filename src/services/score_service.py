class ScoreService:
  """Class for editing score"""

  def add_measure(self, score):
    score.get_staff().add_measure()

score_service = ScoreService()