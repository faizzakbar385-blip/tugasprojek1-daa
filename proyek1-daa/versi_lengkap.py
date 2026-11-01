from kasus_e import gabung


class KMPRekursif:
    def __init__(self, pola):
        self.pola = pola
        self.operasi = 0
        self.lps = [0] * len(pola)
        self._isi_lps(1, 0)

    def _isi_lps(self, i, panjang):
        p = self.pola
        if i >= len(p):
            return
        if p[i] == p[panjang]:
            self.lps[i] = panjang + 1
            self._isi_lps(i + 1, panjang + 1)
        elif panjang != 0:
            self._isi_lps(i, self.lps[panjang - 1])
        else:
            self.lps[i] = 0
            self._isi_lps(i + 1, 0)

    def cari_semua(self, teks):
        hasil = []
        self._cari(teks, 0, 0, hasil)
        return hasil

    def _cari(self, teks, i, j, hasil):
        if i >= len(teks):
            return
        self.operasi += 1
        m = len(self.pola)
        if teks[i] == self.pola[j]:
            if j + 1 == m:
                hasil.append(i + 1 - m)
                self._cari(teks, i + 1, self.lps[j], hasil)
            else:
                self._cari(teks, i + 1, j + 1, hasil)
        elif j != 0:
            self._cari(teks, i, self.lps[j - 1], hasil)
        else:
            self._cari(teks, i + 1, 0, hasil)


class BruteRekursif:
    def __init__(self, pola):
        self.pola = pola
        self.operasi = 0

    def cari_semua(self, teks):
        hasil = []
        self._geser(teks, 0, hasil)
        return hasil

    def _geser(self, teks, i, hasil):
        if i > len(teks) - len(self.pola):
            return
        if self._cocok(teks, i, 0):
            hasil.append(i)
        self._geser(teks, i + 1, hasil)

    def _cocok(self, teks, i, j):
        if j == len(self.pola):
            return True
        self.operasi += 1
        if teks[i + j] != self.pola[j]:
            return False
        return self._cocok(teks, i, j + 1)


def merge_sort_iteratif(data):
    data = list(data)
    n = len(data)
    lebar = 1
    while lebar < n:
        baru = []
        for awal in range(0, n, 2 * lebar):
            kiri = data[awal:awal + lebar]
            kanan = data[awal + lebar:awal + 2 * lebar]
            baru.extend(gabung(kiri, kanan))
        data = baru
        lebar *= 2
    return data


def bubble_sort_rekursif(data):
    data = list(data)
    _bubble(data, len(data))
    return data


def _bubble(data, n):
    if n <= 1:
        return
    for j in range(n - 1):
        if data[j].frekuensi > data[j + 1].frekuensi:
            data[j], data[j + 1] = data[j + 1], data[j]
    _bubble(data, n - 1)