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
