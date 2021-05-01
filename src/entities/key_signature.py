from utils.constants import KEY_SIGNATURES

class KeySignature:
  """Class for getting and setting the key signature

  Attributes:
    key_signature_index: Index of key signature defined in utils/constants.py-file
  """
  def __init__(self, key_signature_index):
    """Constructor for KeySignature class

    Args:
        key_signature_index (int): Index of key signature defined in utils/constants.py-file
    """
    self._key_signature = KEY_SIGNATURES[key_signature_index]

  def get_key_signature(self):
    """Return the key signature in string format

    Returns:
        str: key signature
    """
    return self._key_signature

  def set_key_signature(self, key_signature_index):
    """Sets the key signature with key_signature_index

    Args:
        key_signature_index (int): Index of key signature defined in utils/constants.py-file
    """
    self._key_signature = KEY_SIGNATURES[key_signature_index]
