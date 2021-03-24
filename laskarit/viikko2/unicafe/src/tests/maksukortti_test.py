import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
  def setUp(self):
    self.maksukortti = Maksukortti(10)

  def test_luotu_kortti_on_olemassa(self):
    self.assertNotEqual(self.maksukortti, None)
    
# Kortin saldo alussa oikein
  def test_kortin_saldo_alussa_oikein(self):
    self.assertEqual(str(self.maksukortti), "saldo: 0.1")

# Rahan lataaminen kasvattaa saldoa oikein
  def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
    self.maksukortti.lataa_rahaa(140)
    self.assertEqual(str(self.maksukortti), "saldo: 1.5")

# Rahan ottaminen toimii
# Saldo vähenee oikein, jos rahaa on tarpeeksi
  def test_saldo_vahenee_jos_rahaa_on_tarpeeksi(self):
    self.maksukortti.lataa_rahaa(990)
    self.maksukortti.ota_rahaa(500)
    self.assertEqual(str(self.maksukortti), "saldo: 5.0")

# Saldo ei muutu, jos rahaa ei ole tarpeeksi
  def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
    self.maksukortti.ota_rahaa(100)
    self.assertEqual(str(self.maksukortti), "saldo: 0.1")    

# Metodi palauttaa True, jos rahat riittivät ja muuten False
  def test_palauta_true_jos_rahaa_tarpeeksi(self):
    self.maksukortti.lataa_rahaa(990)
    self.assertEqual(bool(self.maksukortti.ota_rahaa(500)), True)

  def test_palauta_false_jos_raha_ei_riita(self):
    self.assertEqual(bool(self.maksukortti.ota_rahaa(500)), False)

