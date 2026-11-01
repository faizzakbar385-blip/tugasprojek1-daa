class BruteForceMatcher:
    def __init__(self, pola):
        self.pola = pola
        self.operasi = 0

    def cari_semua(self, teks):
        hasil = []
        n, m = len(teks), len(self.pola)
        for i in range(n - m + 1):
            j = 0
            while j < m:
                self.operasi += 1
                if teks[i + j] != self.pola[j]:
                    break
                j += 1
            if j == m:
                hasil.append(i)
        return hasil


class HasilPola:
    def __init__(self, pola):
        self.pola = pola
        self.baris = []
        self.frekuensi = 0


def bubble_sort(data):
    data = list(data)
    n = len(data)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if data[j].frekuensi > data[j + 1].frekuensi:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


class LogAnalyzerBrute:
    def __init__(self, daftar_baris):
        self.baris = daftar_baris

    def analisis(self, daftar_pola):
        semua, total_operasi = [], 0
        for pola in daftar_pola:
            bf = BruteForceMatcher(pola)
            h = HasilPola(pola)
            for no in range(len(self.baris)):
                posisi = bf.cari_semua(self.baris[no])
                if len(posisi) > 0:
                    h.baris.append(no + 1)
                    h.frekuensi += len(posisi)
            total_operasi += bf.operasi
            semua.append(h)
        return bubble_sort(semua), total_operasi


if __name__ == "__main__":
    with open("case5_server_access.txt", encoding="utf-8") as f:
        baris = f.read().split("\n")

    pola = ["POST /healthcheck", "X11; Linux x86_64; rv:130.0", "340.213.18.221:2816"]
    hasil, ops = LogAnalyzerBrute(baris).analisis(pola)

    for n, h in enumerate(hasil, 1):
        pertama = h.baris[0] if len(h.baris) > 0 else "-"
        print(f"{n}. Pola: {h.pola} | Baris pertama: {pertama} | Frekuensi: {h.frekuensi}")
    print("Total operasi:", ops)