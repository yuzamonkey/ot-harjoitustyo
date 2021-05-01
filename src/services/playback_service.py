import time
import pygame
from services.score_service import score_service

class PlaybackService():
  """Class for handling playback
  """
  def __init__(self):
    """Constructor for Playback class. Initializes pygame mixer and sets play variable to False
    """
    pygame.mixer.init()
    self._play = False

  def play(self):
    """Plays the score. The score is returned from score_service 
    """
    score = score_service.get_score()

    tempo = score.get_tempo()
    measures = score.get_staff().get_measures()
    beat_unit = measures[0].get_time_signature().get_beat_unit()

    self._play = True

    for measure in measures:
      for i in range (len(measure.get_notations())):
        if not self._play:
          break
        notation = measure.get_notations()[i]
        if notation.is_note():
          pygame.mixer.music.load(f"./src/utils/wavsounds/{notation.get_pitch()}.wav")
          pygame.mixer.music.play(loops=0)
        time.sleep((beat_unit/notation.get_length()) * (60 / tempo))

    self._play = False

  def stop(self):
    """Stops the playback
    """
    self._play = False

playback_service = PlaybackService()
