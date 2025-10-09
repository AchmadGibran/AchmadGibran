class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.buku_list = []     # koleksi buku
        self.anggota_list = []  # daftar anggota
        self.peminjaman_list = []  # daftar peminjaman

    def tambah_buku(self, buku):
        self.buku_list.append(buku)
        print(f"[INFO] Buku '{buku.judul}' ditambahkan ke {self.nama}")

    def daftar_anggota(self, anggota):
        self.anggota_list.append(anggota)
        print(f"[INFO] Anggota '{anggota.nama}' terdaftar di {self.nama}")

    def pinjam_buku(self, anggota, buku, tanggal_pinjam):
        if buku.status_pinjam == False:
            peminjaman = Peminjaman(anggota, buku, tanggal_pinjam)
            self.peminjaman_list.append(peminjaman)
            buku.status_pinjam = True
            print(f"[PINJAM] {anggota.nama} berhasil meminjam buku '{buku.judul}' pada {tanggal_pinjam}")
        else:
            print(f"[GAGAL] Buku '{buku.judul}' sedang dipinjam orang lain.")

    def tampilkan_status(self):
        print("\n===== STATUS PERPUSTAKAAN =====")
        print(f"Nama Perpustakaan : {self.nama}")

        print("\n--- Koleksi Buku ---")
        for buku in self.buku_list:
            status = "Dipinjam" if buku.status_pinjam else "Tersedia"
            print(f"- {buku.judul} ({buku.penulis}) [{status}]")

        print("\n--- Daftar Anggota ---")
        for anggota in self.anggota_list:
            print(f"- {anggota.nama}")

        print("\n--- Daftar Peminjaman ---")
        if not self.peminjaman_list:
            print("Belum ada transaksi peminjaman.")
        else:
            for p in self.peminjaman_list:
                print(f"- {p.anggota.nama} meminjam '{p.buku.judul}' pada {p.tanggal_pinjam}")
        print("===============================")


class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.status_pinjam = False  # False = tersedia, True = sedang dipinjam


class Anggota:
    def __init__(self, nama):
        self.nama = nama


class Peminjaman:
    def __init__(self, anggota, buku, tanggal_pinjam):
        self.anggota = anggota
        self.buku = buku
        self.tanggal_pinjam = tanggal_pinjam


# ===== PROGRAM UTAMA (TESTING) =====
perpus = Perpustakaan("Perpustakaan Kampus")

# Membuat buku dan anggota
buku1 = Buku("Pemrograman Python", "andi")
buku2 = Buku("Struktur Data", "Budi")
anggota1 = Anggota("Gibran")
anggota2 = Anggota("Bram")

# Menambah buku & anggota
perpus.tambah_buku(buku1)
perpus.tambah_buku(buku2)
perpus.daftar_anggota(anggota1)
perpus.daftar_anggota(anggota2)

# Peminjaman
perpus.pinjam_buku(anggota1, buku1, 
                   "2025-10-02")
perpus.pinjam_buku(anggota2, buku1, "2025-10-03")  # gagal

# Tampilkan status perpustakaan
perpus.tampilkan_status()
