KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not self.__validoi_luku(kapasiteetti) or not self.__validoi_luku(kasvatuskoko):
            raise Exception("Forbidden input")

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def __validoi_luku(self, input, minimum = 0):
        return isinstance(input, int) and input > minimum


    # Jos luku löytyy, palauttaa metodi luvu indexin.
    # Jos luku ei löydy, palauttaa metodi None
    def __etsi_luku(self, luku_etsittavaksi):
        for index in range(0, self.alkioiden_lkm):
            if luku_etsittavaksi == self.lukujono[index]:
                return index
        
        return None

    # Palauttaa True/False: onko luku lukujonossa?
    def kuuluu(self, luku_etsittavaksi):
        return self.__etsi_luku(luku_etsittavaksi) != None

    # Lisää luvun joukkoon. Palauttaa True, kun lisäys onnistunut. False, jos luku oli jo osa joukkoa.
    def lisaa(self, luku_lisattavaksi):
        if self.kuuluu(luku_lisattavaksi):
            return False
        
        self.__liita_listan_loppuun(luku_lisattavaksi)

        if self.alkioiden_lkm  == len(self.lukujono):
            self.__kasvata_taulua()

        return True

    # Lisää monta lukua joukkoon
    def lisaa_monta(self, luvut_lisattavaksi): 
        for luku_lisattavaksi in luvut_lisattavaksi:
            self.lisaa(luku_lisattavaksi)

    # Liittaa luvun listan seuraavaan vapaaseen indeksiin
    def __liita_listan_loppuun(self, luku_liitettavaksi):
        self.lukujono[self.alkioiden_lkm] = luku_liitettavaksi
        self.alkioiden_lkm += 1

    # Kasvattaa taulua
    def __kasvata_taulua(self):
        taulukko_old = self.lukujono
        self.kopioi_taulukko(self.lukujono, taulukko_old)
        self.lukujono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_taulukko(taulukko_old, self.lukujono)

    # Poista halutun luvun joukosta. Palauttaa False, jos lukua ei löydy joukosta. True jos löytyi ja poistettiin.
    def poista(self, luku_poistettavaksi):
        indeksi_poistettavaksi = self.__etsi_luku(luku_poistettavaksi)

        if indeksi_poistettavaksi == None: 
            return False

        self.__siirra_lukuja_vasemmalle(indeksi_poistettavaksi)

        self.alkioiden_lkm -=  1
        return True

    # Siirtää taulun alkioita asekeleen vasemmalle.
    # aloitus_indeksi määrittää, mistä kohdasta eteenpäin taulun alkioita siirretään.
    def __siirra_lukuja_vasemmalle(self, aloitus_indeksi):
        for indeksi in range(aloitus_indeksi, self.alkioiden_lkm - 1):
            apu = self.lukujono[indeksi]
            self.lukujono[indeksi] = self.lukujono[indeksi + 1]
            self.lukujono[indeksi + 1] = apu

    # Kopioi taulun taulu_josta_kopioidaa sisällön tauluun taulu_johon_kopioidaan
    def kopioi_taulukko(self, taulu_josta_kopioidaan, taulu_johon_kopioidaan):
        for i in range(0, len(taulu_josta_kopioidaan)):
            taulu_johon_kopioidaan[i] = taulu_josta_kopioidaan[i]

    # Palauttaa joukon alkioiden lukumäärän
    def mahtavuus(self):
        return self.alkioiden_lkm
    
    # Palauttaa joukon alkiota listana kokonaislukuja
    def to_int_list(self):
        return self.lukujono[0:self.alkioiden_lkm]

    # Palauttaa kahden joukon yhdisteen
    @staticmethod
    def yhdiste(joukko_a, joukko_b):
        joukko_a.lisaa_monta(joukko_b.to_int_list())

        return joukko_a

    # Palauttaa kahden joukon leikkauksen
    @staticmethod
    def leikkaus(joukko_a, joukko_b):
        leikkaus_joukko = IntJoukko()

        taulu = joukko_a.to_int_list() if joukko_a.mahtavuus() >= joukko_b.mahtavuus() else joukko_b.to_int_list()
        vertailu_joukko = joukko_b if joukko_a.mahtavuus() >= joukko_b.mahtavuus() else joukko_a

        for luku in taulu:
            if vertailu_joukko.kuuluu(luku):
                leikkaus_joukko.lisaa(luku)

        return leikkaus_joukko

    # Palauttaa kahden joukon erotuksen
    @staticmethod
    def erotus(joukko_a, joukko_b):
        erotus_joukko = joukko_a

        for luku in joukko_b.to_int_list():
            erotus_joukko.poista(luku)

        return erotus_joukko

    def __str__(self):
        merkkijono = str(self.lukujono[0:self.alkioiden_lkm])
        merkkijono = '{' + merkkijono[1:len(merkkijono)-1] + '}'
        return merkkijono
