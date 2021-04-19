from utils.constants import KEY_SIGNATURES

class KeySignature:
  def __init__(self, key_signature_index):
    self._key_signature = KEY_SIGNATURES[key_signature_index]

  def get_key_signature(self):
    return self._key_signature

  def set_key_signature(self, key_signature_index):
    self._key_signature = KEY_SIGNATURES[key_signature_index]

  def __str__(self):
    return self._key_signature
    