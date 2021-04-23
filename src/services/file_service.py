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

  def get_score_object(self, score_title):
    """Opens existing score to edit"""
    print("Open existing score", score_title)
    name_of_file = f'{score_title}.obj'
    score = score_repository.get_file(name_of_file)
    return score

  def delete_score(self, score_title):
    score_repository.delete_file(f"{score_title}.obj")

  def save_file(self):
    score_to_save = score_service.get_score()
    score_repository.save_score(score_to_save)

  def get_score_names(self):
    scores = score_repository.get_file_names()
    score_names = []
    for name in scores:
      score_names.append(name[:-4])
    return score_names

file_service = FileService()
