from utils.constants import TIME_SIGNATURES

class TimeSignature:
  """Class for getting and setting the time signature

  Attributes:
    time_signature_index: Index of time signature defined in utils/constants.py-file
  """
  def __init__(self, time_signature_index):
    """Constructor for TimeSignature class

    Args:
        time_signature_index (int): Index of time signature defined in utils/constants.py-file
    """
    self._time_signature = TIME_SIGNATURES[time_signature_index]

  def get_time_signature(self):
    """Return the time signature in string format

    Returns:
        str: time signature
    """
    return self._time_signature

  def set_time_signature(self, time_signature_index):
    """Sets the time signature with time_signature_index

    Args:
        time_signature_index (int): Index of time signature defined in utils/constants.py-file
    """
    self._time_signature = TIME_SIGNATURES[time_signature_index]

  def get_beats_per_measure(self):
    """Returns how many beats in a measure

    Returns:
        float: beats per measure
    """
    return float(self._time_signature[0:1])

  def get_beat_unit(self):
    """Returns the beat unit

    Returns:
        float: beat unit
    """
    return float(self._time_signature[-1:])
