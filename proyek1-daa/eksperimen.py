import sys
import time
import random
import tracemalloc
from kasus_e import KMPMatcher, merge_sort, HasilPola
from kasus_e_brute import BruteForceMatcher, bubble_sort
from versi_lengkap import (KMPRekursif, BruteRekursif,
                           merge_sort_iteratif, bubble_sort_rekursif)

sys.setrecursionlimit(20000)

with open("case5_server_access.txt", encoding="utf-8") as f:
    baris = f.read().split("\n")
pola_uji = "X11; Linux x86_64; rv:130.0"


def cari_di_baris(kelas, daftar_baris):
    m = kelas(pola_uji)
    for b in daftar_baris:
        m.cari_semua(b)
    return m.operasi


def ukur(fungsi, *args):
    terbaik = None
    for _ in range(3):
        mulai = time.perf_counter()
        fungsi(*args)
        durasi = time.perf_counter() - mulai
        if terbaik is None or durasi < terbaik:
            terbaik = durasi
    tracemalloc.start()
    fungsi(*args)
    _, puncak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return terbaik, puncak / 1024


def kedalaman(fungsi, *args):
    depth, maks = 0, 0

    def profil(frame, event, arg):
        nonlocal depth, maks
        if event == "call":
            depth += 1
            if depth > maks:
                maks = depth
        elif event == "return":
            depth -= 1

    sys.setprofile(profil)
    fungsi(*args)
    sys.setprofile(None)
    return maks


def buat_data(n):
    random.seed(7)
    data = []
    for _ in range(n):
        h = HasilPola("x")
        h.frekuensi = random.randint(0, 1000)
        data.append(h)
    return data


print("=== PENCARIAN POLA (waktu detik | memori puncak KB) ===")
pencarian = [("KMP iteratif ", KMPMatcher), ("KMP rekursif ", KMPRekursif),
             ("Brute iteratif ", BruteForceMatcher), ("Brute rekursif ", BruteRekursif)]
for jumlah in [500, 1000, 2000, len(baris)]:
    print("Jumlah baris log:", jumlah)
    for nama, kelas in pencarian:
        w, m = ukur(cari_di_baris, kelas, baris[:jumlah])
        print(f"   {nama}: {w:.4f} s | {m:.1f} KB")

print()
print("=== PENGURUTAN (waktu detik | memori puncak KB) ===")
pengurutan = [("Bubble iteratif ", bubble_sort), ("Bubble rekursif ", bubble_sort_rekursif),
              ("Merge rekursif  ", merge_sort), ("Merge iteratif  ", merge_sort_iteratif)]
for n in [250, 500, 1000, 2000]:
    print("n =", n)
    data = buat_data(n)
    for nama, fungsi in pengurutan:
        w, m = ukur(fungsi, data)
        print(f"   {nama}: {w:.4f} s | {m:.1f} KB")

print()
print("=== KEDALAMAN PANGGILAN MAKSIMUM (indikasi overhead stack) ===")
for nama, kelas in pencarian:
    k = kedalaman(cari_di_baris, kelas, baris[:1])
    print(f"   Pencarian {nama}: {k}")
data = buat_data(500)
for nama, fungsi in pengurutan:
    k = kedalaman(fungsi, data)
    print(f"   Pengurutan {nama}: {k}")