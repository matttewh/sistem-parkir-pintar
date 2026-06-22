from parkir import *

buat_csv()
load_data()

while True:

    print("""
=============================
SISTEM PARKIR PINTAR
=============================
1. Tambahkan Kendaraan
2. Tampilkan Data
3. Cari Kendaraan
4. Update Kendaraan
5. Kendaraan Keluar
6. Urutkan Plat
7. Lihat Queue Masuk
8. Lihat Stack Keluar
9. Lihat Pendapatan
10. Keluar
=============================
""")

    pilih = input("Pilih menu : ")

    if pilih == "1":

        tambah_kendaraan()

        input("\nTekan Enter untuk kembali...")

    elif pilih == "2":

        tampilkan_data()

        input("\nTekan Enter untuk kembali...")

    elif pilih == "3":

        cari_kendaraan()

        input("\nTekan Enter untuk kembali...")

    elif pilih == "4":

        update_kendaraan()

        input("\nTekan Enter untuk kembali...")

    elif pilih == "5":

        hapus_kendaraan()

        input("\nTekan Enter untuk kembali...")

    elif pilih == "6":

        sorting_plat()

        input("\nTekan Enter untuk kembali...")

    elif pilih == "7":

        print("\n=== QUEUE KENDARAAN MASUK ===")

        if len(antrian_masuk) == 0:

            print("Queue kosong")

        else:

            for i in antrian_masuk:

                print(i)

        input("\nTekan Enter untuk kembali...")

    elif pilih == "8":

        print("\n=== STACK KENDARAAN KELUAR ===")

        if len(stack_keluar) == 0:

            print("Stack kosong")

        else:

            for i in reversed(stack_keluar):

                print(i)

        input("\nTekan Enter untuk kembali...")

    elif pilih == "9":

        lihat_pendapatan()

        input("\nTekan Enter untuk kembali...")

    elif pilih == "10":

        print("Program selesai")

        break

    else:

        print("Pilihan tidak tersedia")