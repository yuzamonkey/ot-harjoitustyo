import unittest
from entities.score import Score

class TestStaff(unittest.TestCase):
  def setUp(self):
    self.score = Score('TestScore')
    self.staff = self.score.get_staff()

  def test_score_has_staff(self):
    self.assertNotEqual(self.staff, None)

  def test_add_measure_increases_length_of_measures(self):
    staff_length_first = len(self.staff.get_measures())
    self.staff.add_measure()
    staff_length_after = len(self.staff.get_measures())
    self.assertEqual(staff_length_after, staff_length_first+1)

  def test_new_measure_has_previous_measures_attributes(self):
    self.staff.add_measure()
    last_index = len(self.staff.get_measures())-1
    self.assertEqual(
      (self.staff.get_measures()[last_index].get_clef().get_clef()),
      (self.staff.get_measures()[last_index-1].get_clef().get_clef()),
    )
    self.assertEqual(
      self.staff.get_measures()[last_index].get_key_signature().get_key_signature(),
      self.staff.get_measures()[last_index-1].get_key_signature().get_key_signature(),
    )
    self.assertEqual(
      self.staff.get_measures()[last_index].get_time_signature().get_time_signature(),
      self.staff.get_measures()[last_index-1].get_time_signature().get_time_signature(),
    )
  
  def test_overflown_notations_are_removed_after_time_signature_change(self):
    measure = self.staff.get_measures()[0]
    self.assertEqual(measure.get_time_signature().get_time_signature(), '4/4')
    measure.add_note(1, 0)
    measure.add_note(0, 0)
    measure.add_note(1, 0)
    self.assertEqual(measure.measure_is_full(), True)
    self.staff.change_time_signature(0)
    self.assertEqual(measure.get_time_signature().get_time_signature(), '2/4')
    self.assertEqual(measure.measure_is_full(), False)
