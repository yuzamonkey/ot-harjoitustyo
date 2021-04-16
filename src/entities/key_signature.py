class KeySignature:
  def __init__(self, key_signature):
    self._key_signature = key_signature

  def get_key_signature(self):
    return self._key_signature

  def __str__(self):
    return self._key_signature
    