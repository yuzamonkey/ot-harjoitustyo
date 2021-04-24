import unittest
from entities.score import Score

class TestScore(unittest.TestCase):
  def setUp(self):
    self.score = Score('TestScore')

  def test_score_exists(self):
    self.assertNotEqual(self.score, None)

  def test_score_name_is_correct(self):
    self.assertEqual(self.score.get_title(), 'TestScore')

  def test_tempo_changes(self):
    self.score.set_tempo(100)
    tempo_first = self.score.get_tempo()
    self.score.set_tempo(150)
    tempo_after = self.score.get_tempo()
    self.assertNotEqual(tempo_after, tempo_first)
    self.assertEqual(tempo_first, 100)
    self.assertEqual(tempo_after, 150)
