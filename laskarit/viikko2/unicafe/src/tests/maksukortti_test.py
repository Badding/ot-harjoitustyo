import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_alussa_saldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)
    
    def test_saldo_kasvaa_oikein(self):
        self.maksukortti.lataa_rahaa(2555)
        self.assertEqual(self.maksukortti.saldo_euroina(), 35.55)
    
    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(123)
        self.assertEqual(self.maksukortti.saldo_euroina(), 8.77)
    
    def test_saldo_pysyy_samana_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(10000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)
    
    def test_onnistunut_otto_palauttaa_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(100), True)
    
    def test_epaonnistunut_otto_palauttaa_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(10000), False)
    
    def test_str_tulostus_toimii(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")