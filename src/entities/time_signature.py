from utils.constants import TIME_SIGNATURES

class TimeSignature:
  def __init__(self, time_signature_index):
    self._time_signature = TIME_SIGNATURES[time_signature_index]

  def get_time_signature(self):
    return self._time_signature

  def set_time_signature(self, time_signature_index):
    self._time_signature = TIME_SIGNATURES[time_signature_index]

  def get_beats_per_measure(self):
    return float(self._time_signature[0:1])

  def get_beat_unit(self):
    return float(self._time_signature[-1:])

  def __str__(self):
    return self._time_signature
    