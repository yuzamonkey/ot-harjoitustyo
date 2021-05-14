import unittest
from entities.note import Note
from entities.rest import Rest

class TestNotation(unittest.TestCase):
  def setUp(self):
    self.note = Note(0, 0)
    self.rest = Rest(0)

  def test_note_is_note(self):
    self.assertEqual(self.note.is_note(), True)
  
  def test_note_returns_pitch_c2(self):
    self.assertEqual(self.note.get_pitch(), 'c2')

  def test_get_note_returns_note_c(self):
    self.assertEqual(self.note.get_note(), 'c')

  def test_get_pitch_class_returns_2(self):
    self.assertEqual(self.note.get_pitch_class(), '2')

  def test_note_returns_length_2(self):
    self.assertEqual(self.note.get_length(), 2)

  def test_note_set_pitch_changes_pitch(self):
    pitch_first = self.note.get_pitch()
    self.note.set_pitch(1)
    pitch_after = self.note.get_pitch()
    self.assertEqual(pitch_first, 'c2')
    self.assertEqual(pitch_after, 'd2')

  def test_change_length_on_note_changes_length(self):
    length_first = self.note.get_length()
    self.note.set_length(1)
    length_after = self.note.get_length()
    self.assertEqual(length_first, 2)
    self.assertEqual(length_after, 4)

  def test_rest_is_not_note(self):
    self.assertEqual(self.rest.is_note(), False)

  def test_rest_returns_length_2(self):
    self.assertEqual(self.rest.get_length(), 2)
  
  def test_change_length_on_rest_changes_length(self):
    length_first = self.rest.get_length()
    self.rest.set_length(1)
    length_after = self.rest.get_length()
    self.assertEqual(length_first, 2)
    self.assertEqual(length_after, 4)
