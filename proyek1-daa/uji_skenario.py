from kasus_e import KMPMatcher
from kasus_e_brute import BruteForceMatcher


def uji(nama, teks, pola):
    kmp = KMPMatcher(pola)
    bf = BruteForceMatcher(pola)
    h1 = kmp.cari_semua(teks)
    h2 = bf.cari_semua(teks)
    print(nama)
    print("  hasil sama:", h1 == h2, "| KMP:", kmp.operasi, "| Brute:", bf.operasi)


N = 100000
uji("Terbaik (huruf awal tidak pernah cocok)", "A" * N, "B" * 50)
uji("Terburuk (hampir cocok terus)", "A" * N, "A" * 49 + "B")