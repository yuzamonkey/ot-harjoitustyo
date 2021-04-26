from entities.score import Score
from services.score_service import score_service
from repositories.score_repository import score_repository

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
    name_of_file = f'{score_title}.obj'
    return score_repository.get_file(name_of_file)

  def delete_score(self, score_title):
    score_repository.delete_file(f"{score_title}.obj")

  def save_file(self):
    current_score = score_service.get_score()
    score_repository.save_score(current_score)

  def get_score_titles(self):
    file_names = score_repository.get_file_names()
    score_names = []
    for name in file_names:
      score_names.append(name[:-4])
    score_names.sort(key=lambda name: name.lower())
    return score_names

file_service = FileService()
