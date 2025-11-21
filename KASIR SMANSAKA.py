# kasir.py

import datetime
import os

# Daftar barang yang tersedia beserta harganya
# Format: { "kode": {"nama": "Nama Barang", "harga": Harga} }
DAFTAR_BARANG = {
    "A01": {"nama": "Buku Tulis Sinar Dunia", "harga": 5000},
    "A02": {"nama": "Pensil 2B Faber-Castell", "harga": 2500},
    "A03": {"nama": "Penghapus Joyko", "harga": 1500},
    "A04": {"nama": "Penggaris 30cm", "harga": 3000},
    "B01": {"nama": "Air Mineral 600ml", "harga": 3500},
    "B02": {"nama": "Roti Coklat", "harga": 6000},
}

def clear_screen():
    """Membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_daftar_barang():
    """Menampilkan semua barang yang tersedia dalam format tabel."""
    print("=" * 40)
    print("|\tDaftar Barang Tersedia\t|")
    print("=" * 40)
    print("| Kode\t| Nama Barang\t\t| Harga\t|")
    print("-" * 40)
    for kode, detail in DAFTAR_BARANG.items():
        # Menggunakan f-string untuk format yang lebih rapi
        print(f"| {kode}\t| {detail['nama']:<22}| Rp{detail['harga']:>6} |")
    print("=" * 40)
    print()

def proses_transaksi():
    """Fungsi utama untuk memproses satu transaksi penuh."""
    keranjang = []
    total_belanja = 0

    while True:
        tampilkan_daftar_barang()
        
        if keranjang:
            print("--- Keranjang Saat Ini ---")
            for item in keranjang:
                print(f"- {item['jumlah']}x {item['nama']} @ Rp{item['harga']} = Rp{item['subtotal']}")
            print(f"--------------------------")
            print(f"Total Sementara: Rp{total_belanja}")
            print("--------------------------\n")

        kode_barang = input("Masukkan Kode Barang (atau ketik 'selesai' untuk bayar): ").upper()

        if kode_barang.lower() == 'selesai':
            if not keranjang:
                print("Keranjang masih kosong.")
                continue
            break

        if kode_barang in DAFTAR_BARANG:
            while True:
                try:
                    jumlah = int(input(f"Masukkan jumlah '{DAFTAR_BARANG[kode_barang]['nama']}': "))
                    if jumlah > 0:
                        break
                    else:
                        print("Jumlah harus lebih dari 0.")
                except ValueError:
                    print("Input tidak valid. Masukkan angka.")
            
            barang = DAFTAR_BARANG[kode_barang]
            subtotal = barang['harga'] * jumlah
            total_belanja += subtotal

            keranjang.append({
                "kode": kode_barang,
                "nama": barang['nama'],
                "harga": barang['harga'],
                "jumlah": jumlah,
                "subtotal": subtotal
            })
            clear_screen()
            print(f"\n>>> Berhasil menambahkan {jumlah}x {barang['nama']} ke keranjang.\n")
        else:
            clear_screen()
            print("\n>>> Kode barang tidak ditemukan. Silakan coba lagi.\n")
    
    # Proses Diskon
    diskon = 0
    persentase_diskon = 10 # dalam persen
    batas_diskon = 50000   # minimum belanja untuk dapat diskon

    if total_belanja >= batas_diskon:
        diskon = int(total_belanja * (persentase_diskon / 100))
        print(f"\nSelamat! Anda mendapatkan diskon {persentase_diskon}% sebesar Rp{diskon}")

    total_setelah_diskon = total_belanja - diskon

    # Proses Pembayaran
    clear_screen()
    print("=" * 40)
    print("|\t\tRincian Belanja\t\t|")
    print("=" * 40)
    for item in keranjang:
        print(f"{item['jumlah']}x {item['nama']:<25} Rp{item['subtotal']:>8}")
    print("-" * 40)
    print(f"{'Subtotal':<28} Rp{total_belanja:>8}")
    if diskon > 0:
        print(f"{'Diskon ({persentase_diskon}%)':<28} -Rp{diskon:>7}")
    print("=" * 40)
    print(f"{'Total Belanja':<28} Rp{total_setelah_diskon:>8}")
    print("=" * 40)

    while True:
        try:
            bayar = int(input("Masukkan jumlah uang pembayaran: Rp "))
            if bayar >= total_setelah_diskon:
                kembalian = bayar - total_setelah_diskon
                break
            else:
                print(f"Uang pembayaran kurang. Kurang Rp{total_setelah_diskon - bayar}")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

    # Cetak Struk
    print("\n\n--- STRUK PEMBAYARAN ---")
    print(f"Waktu: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("------------------------")
    # Buat konten struk sebagai string
    waktu_transaksi = datetime.datetime.now()
    konten_struk = "--- STRUK PEMBAYARAN ---\n"
    konten_struk += f"Waktu: {waktu_transaksi.strftime('%Y-%m-%d %H:%M:%S')}\n"
    konten_struk += "------------------------\n"
    for item in keranjang:
        print(f"{item['jumlah']}x {item['nama']} @{item['harga']}")
    print("------------------------")
    print(f"Subtotal\t: Rp{total_belanja}")
    konten_struk += f"{item['jumlah']}x {item['nama']} @{item['harga']}\n"
    konten_struk += "------------------------\n"
    konten_struk += f"Subtotal\t: Rp{total_belanja}\n"
    if diskon > 0:
        print(f"Diskon\t\t: -Rp{diskon}")
    print(f"Total\t\t: Rp{total_setelah_diskon}")
    print(f"Bayar\t\t: Rp{bayar}")
    print(f"Kembali\t\t: Rp{kembalian}")
    print("------------------------")
    print("Terima kasih telah berbelanja!")
    print("--- --- --- --- --- --- ---\n")
    konten_struk += f"Diskon\t\t: -Rp{diskon}\n"
    konten_struk += f"Total\t\t: Rp{total_setelah_diskon}\n"
    konten_struk += f"Bayar\t\t: Rp{bayar}\n"
    konten_struk += f"Kembali\t\t: Rp{kembalian}\n"
    konten_struk += "------------------------\n"
    konten_struk += "Terima kasih telah berbelanja!\n"
    konten_struk += "--- --- --- --- --- --- ---\n"

    # 1. Cetak struk ke layar
    print("\n\n" + konten_struk)

    # 2. Simpan struk ke file teks
    try:
        nama_file = f"struk_{waktu_transaksi.strftime('%Y%m%d_%H%M%S')}.txt"
        with open(nama_file, 'w') as file:
            file.write(konten_struk)
        print(f"Struk berhasil disimpan ke file: {nama_file}\n")
    except IOError as e:
        print(f"Gagal menyimpan struk ke file: {e}\n")



if __name__ == "__main__":
    while True:
        proses_transaksi()
        lanjut = input("Mulai transaksi baru? (y/n): ").lower()
        if lanjut != 'y':
            print("Menutup aplikasi kasir...")
            break
        clear_screen()
