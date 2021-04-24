import time
import pygame
from services.score_service import score_service

class PlaybackService():
  def __init__(self):
    pygame.mixer.init()

  def play(self):
    tempo = score_service.get_score().get_tempo()
    measures = score_service.get_score().get_staff().get_measures()
    beat_unit = measures[0].get_time_signature().get_beat_unit()
    for measure in measures:
      for i in range (len(measure.get_notations())):
        notation = measure.get_notations()[i]
        if notation.is_note():
          pygame.mixer.music.load(f"./src/utils/sounds/{notation.get_pitch()}.mp3")
          pygame.mixer.music.play(loops=0)

        time.sleep((beat_unit/notation.get_length()) * (60 / tempo))

  def stop(self):
    pygame.mixer.music.stop()

playback_service = PlaybackService()
