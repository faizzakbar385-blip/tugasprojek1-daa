class KMPMatcher:
    def __init__(self, pola):
        self.pola = pola
        self.lps = self._buat_lps()
        self.operasi = 0

    def _buat_lps(self):
        p = self.pola
        lps = [0] * len(p)
        panjang, i = 0, 1
        while i < len(p):
            if p[i] == p[panjang]:
                panjang += 1
                lps[i] = panjang
                i += 1
            elif panjang != 0:
                panjang = lps[panjang - 1]
            else:
                i += 1
        return lps

    def cari_semua(self, teks):
        hasil, i, j, m = [], 0, 0, len(self.pola)
        while i < len(teks):
            self.operasi += 1
            if teks[i] == self.pola[j]:
                i += 1
                j += 1
                if j == m:
                    hasil.append(i - m)
                    j = self.lps[j - 1]
            elif j != 0:
                j = self.lps[j - 1]
            else:
                i += 1
        return hasil


class HasilPola:
    def __init__(self, pola):
        self.pola = pola
        self.baris = []
        self.frekuensi = 0


def gabung(kiri, kanan):
    hasil, i, j = [], 0, 0
    while i < len(kiri) and j < len(kanan):
        if kiri[i].frekuensi <= kanan[j].frekuensi:
            hasil.append(kiri[i])
            i += 1
        else:
            hasil.append(kanan[j])
            j += 1
    while i < len(kiri):
        hasil.append(kiri[i])
        i += 1
    while j < len(kanan):
        hasil.append(kanan[j])
        j += 1
    return hasil


def merge_sort(data):
    if len(data) <= 1:
        return data
    tengah = len(data) // 2
    return gabung(merge_sort(data[:tengah]), merge_sort(data[tengah:]))


class LogAnalyzer:
    def __init__(self, daftar_baris):
        self.baris = daftar_baris

    def analisis(self, daftar_pola):
        semua, total_operasi = [], 0
        for pola in daftar_pola:
            kmp = KMPMatcher(pola)
            h = HasilPola(pola)
            for no in range(len(self.baris)):
                posisi = kmp.cari_semua(self.baris[no])
                if len(posisi) > 0:
                    h.baris.append(no + 1)
                    h.frekuensi += len(posisi)
            total_operasi += kmp.operasi
            semua.append(h)
        return merge_sort(semua), total_operasi

if __name__ == "__main__":
    with open("case5_server_access.txt", encoding="utf-8") as f:
        baris = f.read().split("\n")

    pola = ["POST /healthcheck", "X11; Linux x86_64; rv:130.0", "340.213.18.221:2816"]
    hasil, ops = LogAnalyzer(baris).analisis(pola)

    print("=== LAPORAN ANOMALI LOG SERVER (TERURUT DARI PALING LANGKA) ===")
    for n, h in enumerate(hasil, 1):
        pertama = h.baris[0] if len(h.baris) > 0 else "-"
        print(f'{n}. Pola: "{h.pola}"')
        print(f"   Indeks Pertama: {pertama}")
        print(f"   Frekuensi: {h.frekuensi}")
        print()
    print("Metrik Eksekusi:")
    print(f"- Total Operasi Dasar (Perbandingan Karakter): {ops} operasi")