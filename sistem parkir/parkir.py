import csv
import os
import math

from datetime import datetime

from collections import deque

from LinkedList import LinkedList


FILE = "kendaraan.csv"

data_parkir = LinkedList()

antrian_masuk = deque()

stack_keluar = []

total_pendapatan = 0


def buat_csv():

    if not os.path.exists(FILE):

        with open(FILE, "w", newline="") as f:

            writer = csv.writer(f)

            writer.writerow([

                "id",

                "plat",

                "pemilik",

                "jenis",

                "jam_masuk"

            ])


def load_data():

    data_parkir.head = None

    if not os.path.exists(FILE):

        return

    with open(FILE, "r", newline="") as f:

        reader = csv.DictReader(f)

        for row in reader:

            data_parkir.tambah(row)


def simpan_csv():

    data = []

    current = data_parkir.head

    while current:

        data.append(current.data)

        current = current.next

    with open(FILE, "w", newline="") as f:

        fieldnames = [

            "id",

            "plat",

            "pemilik",

            "jenis",

            "jam_masuk"

        ]

        writer = csv.DictWriter(

            f,

            fieldnames=fieldnames

        )

        writer.writeheader()

        writer.writerows(data)


def tambah_kendaraan():

    plat = input("Plat : ")

    pemilik = input("Pemilik : ")

    while True:

        jenis = input("Jenis (Motor/Mobil) : ")

        if jenis.lower() in ["motor", "mobil"]:

            break

        print("Masukkan Motor atau Mobil!")

    id_baru = 1

    current = data_parkir.head

    while current:

        id_baru += 1

        current = current.next

    kendaraan = {

        "id": str(id_baru),

        "plat": plat,

        "pemilik": pemilik,

        "jenis": jenis,

        "jam_masuk": datetime.now().strftime(

            "%Y-%m-%d %H:%M:%S"

        )

    }

    data_parkir.tambah(kendaraan)

    antrian_masuk.append(plat)

    simpan_csv()

    print("Data berhasil ditambahkan")


def tampilkan_data():

    if data_parkir.head is None:

        print("Data parkir kosong")

        return

    current = data_parkir.head

    print("\n=== DATA PARKIR ===")

    while current:

        d = current.data

        print(

            "ID:", d["id"],

            "| Plat:", d["plat"],

            "| Pemilik:", d["pemilik"],

            "| Jenis:", d["jenis"],

            "| Jam Masuk:", d["jam_masuk"]

        )

        current = current.next


def cari_kendaraan():

    plat = input("Masukkan plat : ")

    hasil = data_parkir.cari(plat)

    if hasil:

        print(hasil)

    else:

        print("Data tidak ditemukan")


def update_kendaraan():

    plat = input("Plat kendaraan : ")

    hasil = data_parkir.cari(plat)

    if hasil is None:

        print("Data tidak ditemukan")

        return

    pemilik_baru = input("Pemilik baru : ")

    jenis_baru = input("Jenis baru : ")

    data_parkir.update(

        plat,

        pemilik_baru,

        jenis_baru

    )

    simpan_csv()

    print("Data berhasil diupdate")


def sorting_plat():

    data = data_parkir.to_list()

    n = len(data)

    for i in range(n):

        for j in range(n - i - 1):

            if data[j]["plat"] > data[j + 1]["plat"]:

                data[j], data[j + 1] = (

                    data[j + 1],

                    data[j]

                )

    print("\n=== DATA TERURUT ===")

    for d in data:

        print(

            d["id"],

            d["plat"],

            d["pemilik"],

            d["jenis"],

            d["jam_masuk"]

        )


def hitung_biaya(jenis, lama_jam):

    if jenis.lower() == "motor":

        biaya = 3000

        if lama_jam > 1:

            biaya += (lama_jam - 1) * 3000

    else:

        biaya = 5000

        if lama_jam > 1:

            biaya += (lama_jam - 1) * 5000

    return biaya


def hapus_kendaraan():

    plat = input("Plat keluar : ")

    data = data_parkir.cari(plat)

    if data is None:

        print("Data tidak ditemukan")

        return

    masuk = datetime.strptime(

        data["jam_masuk"],

        "%Y-%m-%d %H:%M:%S"

    )

    keluar = datetime.now()

    lama_jam = (

        keluar - masuk

    ).total_seconds() / 3600

    if lama_jam < 1:

        lama_jam = 1

    lama_jam = math.ceil(lama_jam)

    biaya = hitung_biaya(

        data["jenis"],

        lama_jam

    )

    global total_pendapatan

    total_pendapatan += biaya

    print("\n=== STRUK PARKIR ===")

    print("Plat :", data["plat"])

    print("Pemilik :", data["pemilik"])

    print("Jenis :", data["jenis"])

    print("Jam Masuk :", data["jam_masuk"])

    print("Jam Keluar :", keluar.strftime("%Y-%m-%d %H:%M:%S"))

    print("Lama Parkir :", lama_jam, "jam")

    print("Biaya : Rp", biaya)

    data_parkir.hapus(plat)

    stack_keluar.append(plat)

    simpan_csv()

    print("Kendaraan keluar")


def lihat_pendapatan():

    print("\n=== TOTAL PENDAPATAN ===")

    print("Rp", total_pendapatan)
