import sys
import random
from kasus_e import KMPMatcher, merge_sort, HasilPola
from kasus_e_brute import BruteForceMatcher, bubble_sort
from versi_lengkap import (KMPRekursif, BruteRekursif,
                           merge_sort_iteratif, bubble_sort_rekursif)

sys.setrecursionlimit(20000)

with open("case5_server_access.txt", encoding="utf-8") as f:
    baris = f.read().split("\n")


def semua_posisi(matcher):
    hasil = []
    for no in range(len(baris)):
        for pos in matcher.cari_semua(baris[no]):
            hasil.append((no + 1, pos))
    return hasil


pola = ["POST /healthcheck", "X11; Linux x86_64; rv:130.0", "340.213.18.221:2816"]
for p in pola:
    ms = [KMPMatcher(p), KMPRekursif(p), BruteForceMatcher(p), BruteRekursif(p)]
    hs = [semua_posisi(m) for m in ms]
    print(p)
    print("  KMP iter == rekursif :", hs[0] == hs[1])
    print("  Brute iter == rekursif:", hs[2] == hs[3])
    print("  KMP == Brute          :", hs[0] == hs[2])
    print("  operasi (KMP-it, KMP-rek, BF-it, BF-rek):", [m.operasi for m in ms])

random.seed(1)
data = []
for _ in range(300):
    h = HasilPola("x")
    h.frekuensi = random.randint(0, 50)
    data.append(h)

urutan = [
    [h.frekuensi for h in bubble_sort(data)],
    [h.frekuensi for h in bubble_sort_rekursif(data)],
    [h.frekuensi for h in merge_sort(data)],
    [h.frekuensi for h in merge_sort_iteratif(data)],
]
print("Keempat pengurutan sama:", urutan[0] == urutan[1] == urutan[2] == urutan[3])