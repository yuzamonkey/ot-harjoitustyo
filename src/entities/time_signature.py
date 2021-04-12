class TimeSignature:
  def __init__(self, time_signature):
    self._time_signature = time_signature

  def get_time_signature(self):
    return self._time_signature

  def __str__(self):
    return f'Time signature: {self._time_signature}'
    