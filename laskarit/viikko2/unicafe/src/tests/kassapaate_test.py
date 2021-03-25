import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
  def setUp(self):
    self.kassapaate = Kassapaate()

  def test_kassapaate_exists(self):
    self.assertNotEqual(self.kassapaate, None)