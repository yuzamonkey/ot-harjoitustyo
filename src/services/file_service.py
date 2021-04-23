from entities.score import Score
from services.score_service import score_service
from repositories.score_repository import score_repository
import pickle

class FileService:
  """Class for handling score creation, saving, imports and exports"""

  def create_new_score(self):
    """Creates and returns a new score

      Args:
        title: The title of the score
    """
    new_score = Score('Untitled')
    return new_score

  def open_existing_score(self):
    """Opens existing score to edit"""
    print("Open existing score")

  def save_file(self):
    score_to_save = score_service.get_score()
    score_repository.save_score(score_to_save)

file_service = FileService()
