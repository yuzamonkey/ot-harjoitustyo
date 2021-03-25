import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
  def setUp(self):
    self.kassapaate = Kassapaate()
    self.card = Maksukortti(500)

# Luodun kassapäätteen rahamäärä ja myytyjen lounaiden määrä on oikea (rahaa 1000, lounaita myyty 0)
  def test_kassapaate_exists(self):
    self.assertNotEqual(self.kassapaate, None)
  
  def test_kassapaate_saldo_is_correct(self):
    self.assertEqual(int(self.kassapaate.kassassa_rahaa), int(100_000))

  def test_edullinen_purchased_is_zero(self):
    self.assertEqual(self.kassapaate.edulliset, 0)

  def test_maukas_purchased_is_zero(self):
    self.assertEqual(self.kassapaate.edulliset, 0)

# Käteisosto toimii sekä edullisten että maukkaiden lounaiden osalta
# Jos maksu riittävä: 
  # vaihtorahan suuruus on oikea
  def test_buy_edullinen_with_exact_change(self):
    change = self.kassapaate.syo_edullisesti_kateisella(240)
    self.assertEqual(change, 0)

  def test_buy_edullinen_with_change(self):
    change = self.kassapaate.syo_edullisesti_kateisella(340)
    self.assertEqual(change, 100)

  def test_buy_maukas_with_exact_change(self):
    change = self.kassapaate.syo_maukkaasti_kateisella(400)
    self.assertEqual(change, 0)

  def test_buy_maukas_with_change(self):
    change = self.kassapaate.syo_maukkaasti_kateisella(500)
    self.assertEqual(change, 100)

  # kassassa oleva rahamäärä kasvaa lounaan hinnalla
  def test_buying_edullinen_with_cash_increases_amount_of_money_in_kassassa_rahaa(self):
    self.kassapaate.syo_edullisesti_kateisella(500)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
  
  def test_buying_maukas_with_cash_increases_amount_of_money_in_kassassa_rahaa(self):
    self.kassapaate.syo_maukkaasti_kateisella(500)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

  # myytyjen lounaiden määrä kasvaa
  def test_edulliset_increases_after_cash_purchase(self):
    self.kassapaate.syo_edullisesti_kateisella(500)
    self.assertEqual(self.kassapaate.edulliset, 1)

  def test_maukkaat_increases_after_cash_purchase(self):
    self.kassapaate.syo_maukkaasti_kateisella(500)
    self.assertEqual(self.kassapaate.maukkaat, 1)

# Jos maksu ei ole riittävä: 
  # kassassa oleva rahamäärä ei muutu, 
  def test_buy_edullinen_with_too_little_cash_does_not_alter_kassassa_rahaa(self):
    change = self.kassapaate.syo_edullisesti_kateisella(99)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100_000)

  def test_buy_maukas_with_too_little_cash_does_not_alter_kassassa_rahaa(self):
    change = self.kassapaate.syo_maukkaasti_kateisella(99)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100_000)

  # kaikki rahat palautetaan vaihtorahana 
  def test_buy_edullinen_with_too_little_cash_returns_same_value_as_change(self):
    change = self.kassapaate.syo_edullisesti_kateisella(99)
    self.assertEqual(change, 99)

  def test_buy_maukas_with_too_little_cash_returns_same_value_as_change(self):
    change = self.kassapaate.syo_maukkaasti_kateisella(99)
    self.assertEqual(change, 99)
  # myytyjen lounaiden määrässä ei muutosta
  def test_buy_edullinen_with_too_little_cash_does_not_alter_amount_of_sold_edullinen(self):
    change = self.kassapaate.syo_edullisesti_kateisella(99)
    self.assertEqual(self.kassapaate.edulliset, 0)
  
  def test_buy_edullinen_with_too_little_cash_does_not_alter_amount_of_sold_edullinen(self):
    change = self.kassapaate.syo_maukkaasti_kateisella(99)
    self.assertEqual(self.kassapaate.maukkaat, 0)

# Korttiosto toimii sekä edullisten että maukkaiden lounaiden osalta
# Jos tarpeeksi rahaa kortilla
  # veloita summa ja palauta True
  def test_buy_edullinen_decreases_money_from_card(self):
    self.kassapaate.syo_edullisesti_kortilla(self.card)
    self.assertEqual(str(self.card), "saldo: 2.6")
  
  def test_buy_maukas_decreases_money_from_card(self):
    self.kassapaate.syo_maukkaasti_kortilla(self.card)
    self.assertEqual(str(self.card), "saldo: 1.0")

  def test_buy_edullinen_with_card_returns_true(self):
    return_value = self.kassapaate.syo_edullisesti_kortilla(self.card)
    self.assertEqual(return_value, True)

  def test_buy_maukas_with_card_returns_true(self):
    return_value = self.kassapaate.syo_maukkaasti_kortilla(self.card)
    self.assertEqual(return_value, True)
  # myydyt lounaat kasvavat yhdellä
  def test_edulliset_increases_after_card_purchase(self):
    self.kassapaate.syo_edullisesti_kortilla(self.card)
    self.assertEqual(self.kassapaate.edulliset, 1)

  def test_maukkaat_increases_after_card_purchase(self):
    self.kassapaate.syo_maukkaasti_kortilla(self.card)
    self.assertEqual(self.kassapaate.maukkaat, 1)

# Jos ei tarpeeksi rahaa kortilla
  # kortin rahamäärä ei muutu
  def test_buying_edullinen_does_not_alter_amount_of_money_on_card_if_not_enough_money(self):
    self.kassapaate.syo_maukkaasti_kortilla(self.card)
    self.kassapaate.syo_edullisesti_kortilla(self.card)
    self.assertEqual(str(self.card), "saldo: 1.0")
  
  def test_buying_maukas_does_not_alter_amount_of_money_on_card_if_not_enough_money(self):
    self.kassapaate.syo_maukkaasti_kortilla(self.card)
    self.kassapaate.syo_maukkaasti_kortilla(self.card)
    self.assertEqual(str(self.card), "saldo: 1.0")
  # palautetaan False
  def test_buy_edullinen_with_card_returns_false_if_not_enough_money(self):
    self.kassapaate.syo_maukkaasti_kortilla(self.card)
    return_value = self.kassapaate.syo_edullisesti_kortilla(self.card)
    self.assertEqual(return_value, False)
  
  def test_buy_maukas_with_card_returns_false_if_not_enough_money(self):
    self.kassapaate.syo_maukkaasti_kortilla(self.card)
    return_value = self.kassapaate.syo_maukkaasti_kortilla(self.card)
    self.assertEqual(return_value, False)
  # myytyjen lounaiden määrä ei muutu
  def test_buying_edullinen_with_card_does_not_increase_edulliset_if_not_enough_money(self):
    self.kassapaate.syo_maukkaasti_kortilla(self.card)
    self.kassapaate.syo_edullisesti_kortilla(self.card)
    self.assertEqual(self.kassapaate.edulliset, 0)
  
  def test_buying_maukas_with_card_does_not_increase_maukkaat_if_not_enough_money(self):
    self.kassapaate.syo_maukkaasti_kortilla(self.card)
    self.kassapaate.syo_maukkaasti_kortilla(self.card)
    self.assertEqual(self.kassapaate.maukkaat, 1)

# Kassassa oleva rahamäärä ei muutu kortilla ostettaessa
  def test_buying_edullinen_with_card_does_not_change_kassassa_rahaa(self):
    self.kassapaate.syo_edullisesti_kortilla(self.card)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100_000)
  
  def test_buying_maukas_with_card_does_not_change_kassassa_rahaa(self):
    self.kassapaate.syo_maukkaasti_kortilla(self.card)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100_000)

# Kortille rahaa ladattaessa kortin saldo muuttuu ja 
  def test_putting_money_on_card_alters_cards_amount_of_money(self):
    self.kassapaate.lataa_rahaa_kortille(self.card, 100)
    self.assertEqual(str(self.card), "saldo: 6.0")

# kassassa oleva rahamäärä kasvaa ladatulla summalla 
  def test_putting_money_on_card_increases_kassassa_rahaa(self):
    self.kassapaate.lataa_rahaa_kortille(self.card, 100)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100_100)

#lataa negatiivista rahaa ei muuta rahamääriä
  def test_putting_negative_money_on_card_does_not_alter_cards_amount_of_money(self):
    self.kassapaate.lataa_rahaa_kortille(self.card, -100)
    self.assertEqual(str(self.card), "saldo: 5.0")

  def test_put_negative_money_on_card_does_not_increase_kassassa_rahaa(self):
    self.kassapaate.lataa_rahaa_kortille(self.card, -100)
    self.assertEqual(self.kassapaate.kassassa_rahaa, 100_000)