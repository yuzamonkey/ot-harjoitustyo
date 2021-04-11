from entities.score import Score

class FileService:
  """Class for handling file creation, saving, imports and exports"""
  def __init__(self):
    self

  def create_new_file(self):
    """Creates and returns a new file"""
    print("Create new file")
    file = Score()
    return file

  def open_existing_file(self):
    """Opens existing file to edit"""
    print("Open existing file")

file_service = FileService()