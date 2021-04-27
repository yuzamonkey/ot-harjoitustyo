import unittest
from services.score_service import score_service
from entities.score import Score

class TestScoreService(unittest.TestCase):
  def setUp(self):
    self.score = score_service.set_score(Score("TestScore"))

  def test_score_exists(self):
    self.assertNotEqual(score_service.get_score(), None)

  def test_add_measure_increases_length_of_measures(self):
    staff_length_first = score_service.get_staff_length()
    score_service.add_measure()
    staff_length_after = score_service.get_staff_length()
    self.assertEqual(staff_length_after, staff_length_first+1)

  def test_measure_numbers_are_correct(self):
    self.assertEqual(score_service.get_measure_numbers(), [1, 2, 3])

  def test_change_title_changes_title(self):
    title_before = score_service.get_title()
    score_service.set_title('ABCD')
    title_after = score_service.get_title()
    self.assertEqual(title_before, "TestScore")
    self.assertEqual(title_after, "ABCD")
    self.assertNotEqual(title_before, title_after)

  def test_long_title_limits_to_15_chars(self):
    score_service.set_title('abcdefghijklmnopqrstuvwxyz')
    self.assertEqual(score_service.get_title(), 'abcdefghijklmno')

  def test_remove_last_measure_removes_last_measure(self):
    length_before = score_service.get_staff_length()
    score_service.remove_last_measure()
    length_after = score_service.get_staff_length()
    self.assertEqual(length_after, length_before-1)

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

  def test_add_note_returns_false_when_measure_is_full(self):
    measure = 1
    length = 2
    pitch = 'c4'
    return_value1 = score_service.add_note(measure, length, pitch)
    return_value2 = score_service.add_note(measure, length, pitch)
    return_value3 = score_service.add_note(measure, length, pitch)
    self.assertEqual(return_value1, True)
    self.assertEqual(return_value2, True)
    self.assertEqual(return_value3, False)

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
    measure = 0
    length = 999
    return_value = score_service.add_rest(measure, length)
    self.assertEqual(return_value, False)

  def test_add_rest_returns_false_when_measure_is_full(self):
    measure = 1
    length = 2
    return_value1 = score_service.add_rest(measure, length)
    return_value2 = score_service.add_rest(measure, length)
    return_value3 = score_service.add_rest(measure, length)
    self.assertEqual(return_value1, True)
    self.assertEqual(return_value2, True)
    self.assertEqual(return_value3, False)

  def test_change_clef_returns_true_with_valid_input(self):
    new_clef = 'F'
    return_value = score_service.change_clef(new_clef)
    self.assertEqual(return_value, True)

  def test_change_clef_returns_false_with_invalid_input(self):
    new_clef = 'Q'
    return_value = score_service.change_clef(new_clef)
    self.assertEqual(return_value, False)

  def test_change_clef_changes_clef(self):
    clef_first = score_service.get_clef()
    score_service.change_clef('F')
    clef_after = score_service.get_clef()
    self.assertNotEqual(clef_after, clef_first)

  def test_change_key_returns_true_with_valid_input(self):
    new_key = 'F/d'
    return_value = score_service.change_key(new_key)
    self.assertEqual(return_value, True)

  def test_change_key_returns_false_with_invalid_input(self):
    new_key = 'Q/i'
    return_value = score_service.change_key(new_key)
    self.assertEqual(return_value, False)

  def test_change_key_changes_key(self):
    key_first = score_service.get_key_signature()
    score_service.change_key('G/e')
    key_after = score_service.get_key_signature()
    self.assertNotEqual(key_after, key_first)

  def test_change_time_signature_returns_true_with_valid_input(self):
    new_time_signature = '3/4'
    return_value = score_service.change_time_signature(new_time_signature)
    self.assertEqual(return_value, True)

  def test_change_time_signature_returns_false_with_invalid_input(self):
    new_time_signature = '9/3'
    return_value = score_service.change_time_signature(new_time_signature)
    self.assertEqual(return_value, False)

  def test_change_time_signature_changes_time_signature(self):
    time_signature_first = score_service.get_time_signature()
    score_service.change_time_signature('2/4')
    time_signature_after = score_service.get_time_signature()
    self.assertNotEqual(time_signature_after, time_signature_first)
