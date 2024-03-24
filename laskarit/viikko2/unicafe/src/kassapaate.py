class Kassapaate:
    def __init__(self):
        self.kassassa_rahaa = 100000
        self.edulliset = 0
        self.maukkaat = 0
        self.edullinen = 240
        self.maukas = 400

    def syo_edullisesti_kateisella(self, maksu):
        if maksu >= self.edullinen:
            self.kassassa_rahaa = self.kassassa_rahaa + self.edullinen
            self.edulliset += 1
            return maksu - self.edullinen
        else:
            return maksu

    def syo_maukkaasti_kateisella(self, maksu):
        if maksu >= self.maukas:
            self.kassassa_rahaa = self.kassassa_rahaa + self.maukas
            self.maukkaat += 1
            return maksu - self.maukas
        else:
            return maksu

    def syo_edullisesti_kortilla(self, kortti):
        if kortti.saldo >= self.edullinen:
            kortti.ota_rahaa(self.edullinen)
            self.edulliset += 1
            return True
        else:
            return False

    def syo_maukkaasti_kortilla(self, kortti):
        if kortti.saldo >= self.maukas:
            kortti.ota_rahaa(self.maukas)
            self.maukkaat += 1
            return True
        else:
            return False

    def lataa_rahaa_kortille(self, kortti, summa):
        if summa >= 0:
            kortti.lataa_rahaa(summa)
            self.kassassa_rahaa += summa
        else:
            return

    def kassassa_rahaa_euroina(self):
        return self.kassassa_rahaa / 100
