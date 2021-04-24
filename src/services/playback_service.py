from services.score_service import score_service
import pygame
import time

class PlaybackService():
  def __init__(self):
    pygame.mixer.init()

  def play(self):
    measures = score_service.get_score().get_staff().get_measures()
    for measure in measures:
      for i in range (len(measure.get_notations())):
        notation = measure.get_notations()[i]
        if notation.is_note():
          print("NOTE", notation.get_pitch(), notation.get_length())
          pygame.mixer.music.load(f"./src/utils/sounds/{notation.get_pitch()}.mp3")
          pygame.mixer.music.play(loops=0)
        else:
          print("rest", notation.get_length())
        
        time.sleep(notation.get_length()*0.1)

playback_service = PlaybackService()