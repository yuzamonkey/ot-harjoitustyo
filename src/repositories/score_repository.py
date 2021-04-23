import pickle

class ScoreRepository:

  def save_score(self, score):
    file_object = open(f"data/scores/{score.get_title()}.obj", "wb")
    pickle.dump(score, file_object)
    file_object.close()

score_repository = ScoreRepository()