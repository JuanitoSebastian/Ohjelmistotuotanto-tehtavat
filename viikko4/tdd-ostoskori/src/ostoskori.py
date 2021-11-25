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
        if poistettava.nimi not in self._ostokset: return

        self._ostokset[poistettava.nimi].muuta_lukumaaraa(-1)

        lkm = self._ostokset[poistettava.nimi].lukumaara()

        if lkm == 0:
            self._ostokset.pop(poistettava.nimi, None)

    def tyhjenna(self):
        self._ostokset.clear()

    def ostokset(self):
        return list(self._ostokset.values())
