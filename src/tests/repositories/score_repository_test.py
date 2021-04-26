import unittest
from repositories.score_repository import score_repository
from entities.score import Score

class TestScoreRepository(unittest.TestCase):
  def setUp(self):
    score = Score('TestScore')
    score_repository.save_score(score)

  def test_get_file_returns_correct_file(self):
    score = score_repository.get_file('TestScore.obj')
    self.assertNotEqual(score, None)

  def test_get_file_returns_None_for_invalid_file(self):
    score = score_repository.get_file('WrongName.obj')
    self.assertEqual(score, None)

  def test_deleting_file_deletes_file(self):
    score_before = score_repository.get_file('TestScore.obj')
    score_repository.delete_file('TestScore.obj')
    score_after = score_repository.get_file('TestScore.obj')
    self.assertNotEqual(score_before, None)
    self.assertEqual(score_after, None)
