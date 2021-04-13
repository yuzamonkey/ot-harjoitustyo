import unittest
from entities.score import Score

class TestScore(unittest.TestCase):
  def setUp(self):
    self.score = Score('TestScore')

  def test_score_exists(self):
    self.assertNotEqual(self.score, None)

  def test_score_name_is_correct(self):
    self.assertEqual(self.score.get_title(), 'TestScore')
