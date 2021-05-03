import unittest
from entities.measure import Measure
from entities.score import Score

class TestMeasure(unittest.TestCase):
  def setUp(self):
    self.score = Score('TestScore')
    self.measure = self.score.get_staff().get_measures()[0]

  def test_score_exists(self):
    self.assertNotEqual(self.score, None)

  def test_measure_exists(self):
    self.assertNotEqual(self.measure, None)

  def test_get_notations_returns_empty_array(self):
    length = len(self.measure.get_notations())
    self.assertEqual(length, 0)

  def test_measure_is_not_full(self):
    self.assertEqual(self.measure.measure_is_full(), False)

  def test_measure_is_full(self):
    self.measure.add_note(0, 0)
    self.measure.add_note(0, 0)
    self.assertEqual(self.measure.measure_is_full(), True)
