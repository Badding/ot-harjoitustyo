import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassapaattessa_oikea_aloitus_rahaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
    
    def test_lounaita_alussa_molemmat_nolla(self):
        edulliset = self.kassapaate.edulliset
        maukkaat = self.kassapaate.maukkaat
        self.assertEqual(edulliset + maukkaat, 0)

    def test_edullinen_kateisella_kassa_enemman(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)

    def test_maukas_kateisella_kassa_enemman(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004)

    def test_edullinen_kateisella_vaihtorahalla(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)
    
    def test_maukas_kateisella_vaihtorahalla(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(1000), 600)

    def test_edullinen_kateisella_edulliset_myyty_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_maukas_kateisella_maukkaat_myyty_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_kateisella_raha_ei_riita_kaikki_takaisin(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    def test_edullinen_kateisella_raha_ei_riita_myyty_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullinen_kateisella_raha_ei_riita_kassa_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_maukas_kateisella_raha_ei_riita_kaikki_takaisin(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)
    
    def test_maukas_kateisella_raha_ei_riita_myyty_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_maukaasti_kateisella_raha_ei_riita_kassa_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    ### Korttimaksut ###
    
    def test_kassapaate_lataa_rahaa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 20.00)
    
    def test_kassapaate_lataa_rahaa_kortille_negatiivinen_summa(self):
        tulos = self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(tulos, None)

    def test_kassapaate_lataa_rahaa_kortille_kassa_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1005)

    # Edullinen
    def test_edullisesti_kortilla_onnistuu(self):
        oli_rahaa = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(oli_rahaa, True)
    
    def test_edullisesti_kortilla_edulliset_myyty_kasvaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edulliesti_kortilla_rahaa_ei_riita_ei_veloitusta(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo_euroina(), 1.00)
    
    def test_edullisesti_kortilla_rahaa_ei_riita_myyty_ei_kasva(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullisesti_kortilla_rahaa_ei_riita_palauttaa_false(self):
        maksukortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), False)

    def test_edullisesti_kortilla_kassa_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    # Maukas
        
    def test_maukkaasti_kortilla_onnistuu(self):
        oli_rahaa = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(oli_rahaa, True)
    
    def test_maukkaasti_kortilla_maukkaat_myyty_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_maukaasti_kortilla_rahaa_ei_riita_ei_veloitusta(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo_euroina(), 1.00)
    
    def test_maukkaasti_kortilla_rahaa_ei_riita_myyty_ei_kasva(self):
        maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_maukkaasti_kortilla_rahaa_ei_riita_palauttaa_false(self):
        maksukortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), False)
    
    def test_maukkaasti_kortilla_kassa_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)