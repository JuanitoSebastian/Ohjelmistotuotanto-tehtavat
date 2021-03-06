import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_kori_palauttaa_tuotteen_hinnan(self):
        kaura_maito = Tuote("Oatly ikaffe", 2)
        self.kori.lisaa_tuote(kaura_maito)

        self.assertEqual(self.kori.hinta(), 2)

    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        sukat = Tuote("Sukat puuvilla", 5)
        villa_sukat = Tuote("Villasukat", 6)

        self.kori.lisaa_tuote(sukat)
        self.kori.lisaa_tuote(villa_sukat)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_tuotteen_lisaamisen_jalkeen_kori_palauttaa_oikean_hinnan(self):
        sukat = Tuote("Sukat puuvilla", 5)
        villa_sukat = Tuote("Villasukat", 6)

        self.kori.lisaa_tuote(sukat)
        self.kori.lisaa_tuote(villa_sukat)

        self.assertEqual(self.kori.hinta(), 11)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_kori_palauttaa_oikean_hinnan(self):
        mayrakoira = Tuote("Koff 12kpl", 15)
        self.kori.lisaa_tuote(mayrakoira)
        self.kori.lisaa_tuote(mayrakoira)

        self.assertEqual(self.kori.hinta(), 30)

    def test_kahden_saman_tuotteen_lisaaminen_jalkeen_korissa_kaksi_tavaraa(self):
        mayrakoira = Tuote("Koff 12kpl", 15)
        self.kori.lisaa_tuote(mayrakoira)
        self.kori.lisaa_tuote(mayrakoira)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        kahvi = Tuote("Kahvi Columbia", 5)

        self.kori.lisaa_tuote(kahvi)

        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuote, maito)
        self.assertEqual(ostos.lukumaara(), 1)
        self.assertEqual(ostos.hinta(), 3)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosoliota(self):
        suklaa = Tuote("Suklaa", 2)
        punainen_linssi = Tuote("Punaiset linssit", 1)

        self.kori.lisaa_tuote(suklaa)
        self.kori.lisaa_tuote(punainen_linssi)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_yksi_ostos(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_oikeanlaisen_ostoksen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
 
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuote, maito)
        self.assertEqual(ostos.lukumaara(), 2)
        self.assertEqual(ostos.hinta(), 6)

    def test_korissa_kaksi_samaa_tuotetta_toinen_poistetaan_koriin_jaa_ostos_jossa_yksi_tuote(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.kori.poista_tuote(maito)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuote, maito)
        self.assertEqual(ostos.lukumaara(), 1)
        self.assertEqual(ostos.hinta(), 3)
 
    def test_korista_poistetaan_viimeinen_tuote_jaljelle_jaa_tyhja_kori(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.kori.poista_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(len(ostokset), 0)

    def test_korin_tyhjentaminen_jattaa_tyhjan_korin(self):
        maito = Tuote("Maito", 3)
        suklaa = Tuote("Suklaa", 2)
        punainen_linssi = Tuote("Punaiset linssit", 1)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(suklaa)
        self.kori.lisaa_tuote(punainen_linssi)

        self.kori.tyhjenna()

        ostokset = self.kori.ostokset()

        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(len(ostokset), 0)