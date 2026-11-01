import time
from kasus_e import merge_sort, HasilPola
from kasus_e_brute import bubble_sort


def buat_data(daftar_frekuensi):
    data = []
    for f in daftar_frekuensi:
        h = HasilPola("x")
        h.frekuensi = f
        data.append(h)
    return data


def ukur(nama, fungsi, data):
    mulai = time.perf_counter()
    hasil = fungsi(data)
    selesai = time.perf_counter()
    urut = True
    for i in range(len(hasil) - 1):
        if hasil[i].frekuensi > hasil[i + 1].frekuensi:
            urut = False
    print(f"    {nama}: {selesai - mulai:.4f} detik | terurut: {urut}")


for n in [500, 1000, 2000, 4000]:
    print("n =", n)
    kasus = [
        ("Sudah urut (terbaik)", list(range(n))),
        ("Terbalik (terburuk)", list(range(n, 0, -1))),
    ]
    for nama_kasus, isi in kasus:
        print("  ", nama_kasus)
        ukur("Bubble", bubble_sort, buat_data(isi))
        ukur("Merge ", merge_sort, buat_data(isi))