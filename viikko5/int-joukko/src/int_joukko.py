KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetin täytyy olla tyyppiä int sekä suurempi kuin nolla")

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.lukujono

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.lukujono[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

        if self.alkioiden_lkm == len(self.lukujono):
            self.lukujono.append([0] * self.kasvatuskoko)

    def poista(self, n):
        idx = -1
        aux = 0

        for i in range(0, self.alkioiden_lkm):

            if self.lukujono[i] == n:
                idx = i
                self.lukujono[idx] = 0

                for j in range(idx, self.alkioiden_lkm - 1):
                    aux = self.lukujono[j]
                    self.lukujono[j] = self.lukujono[j + 1]
                    self.lukujono[j + 1] = aux

                self.alkioiden_lkm = self.alkioiden_lkm - 1
                break

    def to_int_list(self):
        lukujono = [0] * self.alkioiden_lkm

        for i in range(0, len(lukujono)):
            lukujono[i] = self.lukujono[i]

        return lukujono

    @staticmethod
    def yhdiste(a, b):
        yhdistejoukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            yhdistejoukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            yhdistejoukko.lisaa(b_taulu[i])

        return yhdistejoukko

    @staticmethod
    def leikkaus(a, b):
        leikkausjoukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    leikkausjoukko.lisaa(b_taulu[j])

        return leikkausjoukko

    @staticmethod
    def erotus(a, b):
        erotusjoukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            erotusjoukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            erotusjoukko.poista(b_taulu[i])

        return erotusjoukko

    def __str__(self):
        result = "{"

        for i in range(0, self.alkioiden_lkm - 1):
            result += f"{self.lukujono[i]}, "

        if self.alkioiden_lkm > 0:
            result += f"{self.lukujono[self.alkioiden_lkm - 1]}"
        result += "}"
        return result
