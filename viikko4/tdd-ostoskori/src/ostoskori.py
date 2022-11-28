from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._hinta = 0
        self._tavaroita_korissa = 0
        self._ostokset = []
        self._tuotteet = []

    def tavaroita_korissa(self):
        return self._tavaroita_korissa

    def hinta(self):
        return self._hinta

    def lisaa_tuote(self, lisattava: Tuote):
        if lisattava.nimi() in self._tuotteet:
            for ostos in self._ostokset:
                if ostos.tuotteen_nimi() == lisattava.nimi():
                    ostos.muuta_lukumaaraa(1)
        else:
            ostos = Ostos(lisattava)
            self._ostokset.append(ostos)
            self._tuotteet.append(ostos.tuotteen_nimi())

        self._hinta += lisattava.hinta()
        self._tavaroita_korissa += 1

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostokset
