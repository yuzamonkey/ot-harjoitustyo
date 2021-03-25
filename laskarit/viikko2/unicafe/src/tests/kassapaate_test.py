import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

"""
Luodun kassapäätteen rahamäärä ja myytyjen lounaiden määrä on oikea (rahaa 1000, lounaita myyty 0)
Käteisosto toimii sekä edullisten että maukkaiden lounaiden osalta
Jos maksu riittävä: kassassa oleva rahamäärä kasvaa lounaan hinnalla ja vaihtorahan suuruus on oikea
Jos maksu on riittävä: myytyjen lounaiden määrä kasvaa
Jos maksu ei ole riittävä: kassassa oleva rahamäärä ei muutu, kaikki rahat palautetaan vaihtorahana ja myytyjen lounaiden määrässä ei muutosta
seuraavissa testeissä tarvitaan myös Maksukorttia jonka oletetaan toimivan oikein
Korttiosto toimii sekä edullisten että maukkaiden lounaiden osalta
Jos kortilla on tarpeeksi rahaa, veloitetaan summa kortilta ja palautetaan True
Jos kortilla on tarpeeksi rahaa, myytyjen lounaiden määrä kasvaa
Jos kortilla ei ole tarpeeksi rahaa, kortin rahamäärä ei muutu, myytyjen lounaiden määrä muuttumaton ja palautetaan False
Kassassa oleva rahamäärä ei muutu kortilla ostettaessa
Kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamäärä kasvaa ladatulla summalla
"""

class TestKassapaate(unittest.TestCase):
  def setUp(self):
    self.kassapaate = Kassapaate()
    self.card = Maksukortti(500)

  def test_kassapaate_exists(self):
    self.assertNotEqual(self.kassapaate, None)
  #kassan saldo oikein
  def test_kassapaate_saldo_is_correct(self):
    self.assertEqual(int(self.kassapaate.kassassa_rahaa), int(100_000))
  #edullisia 0
  def test_edullinen_purchased_is_zero(self):
    self.assertEqual(self.kassapaate.edulliset, 0)
  #maukkaita 0
  def test_maukas_purchased_is_zero(self):
    self.assertEqual(self.kassapaate.edulliset, 0)

  #rahamäärä kassassa lisääntyy lounaita ostettaessa käteisellä
  def test_buying_edullinen_with_cash_increases_amount_of_money_in_kassassa_rahaa(self):
    self.kassapaate.syo_edullisesti_kateisella(500)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
  
  def test_buying_maukas_with_cash_increases_amount_of_money_in_kassassa_rahaa(self):
    self.kassapaate.syo_maukkaasti_kateisella(500)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

  #osta edullinen käteisellä edullisen hinnalla
  def test_buy_edullinen_with_exact_change(self):
    change = self.kassapaate.syo_edullisesti_kateisella(240)
    self.assertEqual(change, 0)
  #osta edullinen käteisellä ja palauta ylijäämä raha
  def test_buy_edullinen_with_change(self):
    change = self.kassapaate.syo_edullisesti_kateisella(340)
    self.assertEqual(change, 100)
  #osta edullinen käteisellä liian vähällä rahalla
  def test_buy_edullinen_with_too_little_cash_money(self):
    change = self.kassapaate.syo_edullisesti_kateisella(99)
    self.assertEqual(change, 99)

  #osta maukas käteisellä edullisen hinnalla
  def test_buy_maukas_with_exact_change(self):
    change = self.kassapaate.syo_maukkaasti_kateisella(400)
    self.assertEqual(change, 0)
  #osta maukas käteisellä ja palauta ylijäämä raha
  def test_buy_maukas_with_change(self):
    change = self.kassapaate.syo_maukkaasti_kateisella(500)
    self.assertEqual(change, 100)
  #osta maukas liian vähällä rahalla
  def test_buy_maukas_with_too_little_cash_money(self):
    change = self.kassapaate.syo_maukkaasti_kateisella(99)
    self.assertEqual(change, 99)

# osta kortilla edullinen
  def test_buy_edullinen_with_card_returns_true(self):
    return_value = self.kassapaate.syo_edullisesti_kortilla(self.card)
    self.assertEqual(return_value, True)
# osta kortilla maukas
  def test_buy_maukas_with_card_returns_true(self):
    return_value = self.kassapaate.syo_maukkaasti_kortilla(self.card)
    self.assertEqual(return_value, True)
# osta kortilla edullinen liian vähällä rahalla
  def test_buy_edullinen_with_card_returns_false_if_not_enough_money(self):
    self.kassapaate.syo_maukkaasti_kortilla(self.card)
    return_value = self.kassapaate.syo_edullisesti_kortilla(self.card)
    self.assertEqual(return_value, False)
# osta kortilla maukas liian vähällä rahalla
  def test_buy_maukas_with_card_returns_false_if_not_enough_money(self):
    self.kassapaate.syo_maukkaasti_kortilla(self.card)
    return_value = self.kassapaate.syo_maukkaasti_kortilla(self.card)
    self.assertEqual(return_value, False)


  #edullisten määrä kasvaa, kun ostetaan käteisellä
  def test_edulliset_increases_after_cash_purchase(self):
    self.kassapaate.syo_edullisesti_kateisella(500)
    self.assertEqual(self.kassapaate.edulliset, 1)
  #edullisten määrä kasvaa, kun ostetaan kortilla
  def test_edulliset_increases_after_card_purchase(self):
    self.kassapaate.syo_edullisesti_kortilla(self.card)
    self.assertEqual(self.kassapaate.edulliset, 1)
  #maukkaiden määrä kasvaa, kun ostetaan käteisellä
  def test_maukkaat_increases_after_cash_purchase(self):
    self.kassapaate.syo_maukkaasti_kateisella(500)
    self.assertEqual(self.kassapaate.maukkaat, 1)
  #maukkaiden määrä kasvaa, kun ostetaan kortilla
  def test_maukkaat_increases_after_card_purchase(self):
    self.kassapaate.syo_maukkaasti_kortilla(self.card)
    self.assertEqual(self.kassapaate.maukkaat, 1)

  
  #kassassa oleva rahamäärä ei muutu kortilla ostettaessa
  def test_buying_edullinen_with_card_does_not_change_kassassa_rahaa(self):
    self.kassapaate.syo_edullisesti_kortilla(self.card)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100_000)
  
  def test_buying_maukas_with_card_does_not_change_kassassa_rahaa(self):
    self.kassapaate.syo_maukkaasti_kortilla(self.card)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100_000)
  

  #lataa rahaa kortille
  def test_putting_money_on_card_increases_kassassa_rahaa(self):
    self.kassapaate.lataa_rahaa_kortille(self.card, 100)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100_100)

  def test_putting_money_on_card_changes_cards_amount_of_money(self):
    self.kassapaate.lataa_rahaa_kortille(self.card, 100)
    self.assertEqual(str(self.card), "saldo: 6.0")

  #lataa negatiivista rahaa ei muuta rahamäärää
  def test_putting_negative_money_on_card_does_not_change_cards_amount_of_money(self):
    self.kassapaate.lataa_rahaa_kortille(self.card, -100)
    self.assertEqual(str(self.card), "saldo: 5.0")

  def test_put_negative_money_on_card_does_not_increase_kassassa_rahaa(self):
    self.kassapaate.lataa_rahaa_kortille(self.card, -100)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100_000)