from entities.score import Score

class FileService:
  """Class for handling score creation, saving, imports and exports"""
  def __init__(self):
    self

  def create_new_score(self):
    """Creates and returns a new score

      Args:
        title: The title of the score
    """
    print("Create new score")
    new_score = Score('Untitled')
    return new_score

  def open_existing_score(self):
    """Opens existing score to edit"""
    print("Open existing score")

file_service = FileService()