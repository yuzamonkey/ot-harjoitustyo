import unittest
from services.file_service import file_service

class TestFileService(unittest.TestCase):
  def setUp(self):
    self.new_score = file_service.create_new_score()

  def test_new_score_exists(self):
    self.assertNotEqual(self.new_score, None)

  def test_new_score_name_equals_untitled(self):
    self.assertEqual(self.new_score.get_name(), 'Untitled')
