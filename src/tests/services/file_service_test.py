import unittest
from services.file_service import file_service
from services.score_service import score_service
from repositories.score_repository import score_repository

class TestFileService(unittest.TestCase):
  def setUp(self):
    self.score = file_service.create_new_score()
    score_service.set_score(self.score)
    file_service.save_file()

  def test_new_score_exists(self):
    self.assertNotEqual(self.score, None)

  def test_new_score_name_equals_untitled(self):
    self.assertEqual(self.score.get_title(), 'Untitled')

  def test_get_score_object_returns_score(self):
    score = file_service.get_score_object('Untitled')
    self.assertNotEqual(score, None)

  def test_get_score_object_returns_None_for_invalid_score(self):
    score = file_service.get_score_object('InvalidName')
    self.assertEqual(score, None)

  def test_delete_score_deletes_score(self):
    score_first = file_service.get_score_object('Untitled')
    file_service.delete_score('Untitled')
    score_after = file_service.get_score_object('Untitled')
    self.assertNotEqual(score_first, None)
    self.assertEqual(score_after, None)
