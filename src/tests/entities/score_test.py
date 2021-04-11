import unittest
from entities.score import Score

class TestScore(unittest.TestCase):
  def setUp(self):
    self.score = Score()
  
  def test_score_returns_false(self):
    self.assertEqual(self.score.score_is_selected_for_edit(), False)