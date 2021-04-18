import unittest
from services.score_service import score_service
from entities.score import Score

class TestScoreService(unittest.TestCase):
  def setUp(self):
    self.score = score_service.set_score(Score("TestScore"))

  def test_score_exists(self):
    self.assertNotEqual(score_service.get_score(), None)

  def test_add_measure_increases_length_of_measures(self):
    staff_length_first = score_service.get_length()
    score_service.add_measure()
    staff_length_after = score_service.get_length()
    self.assertEqual(staff_length_after, staff_length_first+1)

  def test_measure_numbers_are_correct(self):
    self.assertEqual(score_service.get_measure_numbers(), [1, 2, 3])

  def test_add_note_returns_true_with_valid_parameters(self):
    measure = 2
    length = 4
    pitch = 'c4'
    return_value = score_service.add_note(measure, length, pitch)
    self.assertEqual(return_value, True)

  def test_add_note_returns_false_with_invalid_measure(self):
    measure = -1
    length = 4
    pitch = 'c4'
    return_value = score_service.add_note(measure, length, pitch)
    self.assertEqual(return_value, False)

  def test_add_note_returns_false_with_invalid_length(self):
    measure = -1
    length = 999
    pitch = 'c4'
    return_value = score_service.add_note(measure, length, pitch)
    self.assertEqual(return_value, False)

  def test_add_note_returns_false_with_invalid_pitch(self):
    measure = -1
    length = 999
    pitch = 'abcd'
    return_value = score_service.add_note(measure, length, pitch)
    self.assertEqual(return_value, False)

  def test_add_rest_returns_true_with_valid_parameters(self):
    measure = 2
    length = 4
    return_value = score_service.add_rest(measure, length)
    self.assertEqual(return_value, True)

  def test_add_rest_returns_false_with_invalid_measure(self):
    measure = -1
    length = 4
    return_value = score_service.add_rest(measure, length)
    self.assertEqual(return_value, False)

  def test_add_rest_returns_false_with_invalid_length(self):
    measure = -1
    length = 999
    return_value = score_service.add_rest(measure, length)
    self.assertEqual(return_value, False)
    