from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._ostokset = {}

    def tavaroita_korissa(self):
        lkm = 0

        for ostos in self._ostokset.values():
            lkm += ostos.lukumaara()
        
        return lkm

    def hinta(self):
        hinta = 0

        for ostos in self._ostokset.values():
            hinta += ostos.hinta()
        
        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        # Tarkistetaan onko tuotetta lisätty jo koriin
        if lisattava.nimi in self._ostokset:
            self._ostokset[lisattava.nimi].muuta_lukumaaraa(1)
            return
        
        # Tuotetta ei lisätty koriin, luodaan uusi ostos
        self._ostokset[lisattava.nimi] = Ostos(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
