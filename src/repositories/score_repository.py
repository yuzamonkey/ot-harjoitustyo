import pickle
import os

class ScoreRepository:

  def get_file(self, file_name):
    try:
      file_object = open(f"data/scores/{file_name}", "rb")
      score_object = pickle.load(file_object)
      file_object.close()
      return score_object
    except NameError:
      print("NO FILE CALLED", file_name)
      return None

  def save_score(self, score):
    file_object = open(f"data/scores/{score.get_title()}.obj", "wb")
    pickle.dump(score, file_object)
    file_object.close()

  def delete_file(self, file_name):
    os.remove(f"./data/scores/{file_name}")

  def get_file_names(self):
    if os.path.exists("./data/scores"):
      for root, dirs, files in os.walk("./data/scores"):
        return files
    else:
      return []

score_repository = ScoreRepository()
