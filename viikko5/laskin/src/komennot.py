class Summa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote

    def suorita(self):
        syotetty_luku = int(self._lue_syote())
        self._sovelluslogiikka.plus(syotetty_luku)

class Erotus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote

    def suorita(self):
        syotetty_luku = int(self._lue_syote())
        self._sovelluslogiikka.miinus(syotetty_luku)

class Nollaus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote

    def suorita(self):
        self._sovelluslogiikka.nollaa()

class Kumoa:
    def __init__(self, sovelluslogiikka, lue_syote, aiemmat_tulokset):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote
        self._aiemmat_tulokset = aiemmat_tulokset

    def suorita(self):
        if len(self._aiemmat_tulokset) == 0: 
            return

        self._sovelluslogiikka.aseta_arvo(self._aiemmat_tulokset.pop())